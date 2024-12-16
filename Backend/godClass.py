import ast
from collections import defaultdict
from radon.complexity import cc_visit


class GodClassDetector(ast.NodeVisitor):
    def __init__(self, file_content):
        self.file_content = file_content  # Store file content
        self.classes = {}

    def visit_ClassDef(self, node):
        class_name = node.name
        methods = [child for child in node.body if isinstance(child, ast.FunctionDef)]
        attributes = set()

        for child in node.body:
            if isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target, ast.Attribute):
                        attributes.add(target.attr)
                    elif isinstance(target, ast.Name):
                        attributes.add(target.id)

        wmc = self.calculate_wmc(methods)
        tcc = self.calculate_tcc(methods, attributes) if len(methods) > 1 else None
        atfd = self.calculate_atfd(methods, class_name)

        self.classes[class_name] = {
            "methods": methods,
            "attributes": attributes,
            "wmc": wmc,
            "tcc": tcc if tcc is not None else "N/A",
            "atfd": atfd,
        }

    def calculate_wmc(self, methods):
        wmc = 0
        for method in methods:
            try:
                # Extract source code for the method
                method_source = ast.get_source_segment(self.file_content, method)
                wmc += sum(block.complexity for block in cc_visit(method_source))
            except Exception as e:
                print(f"Error calculating WMC for method: {method.name}, Error: {e}")
        return wmc

    def calculate_tcc(self, methods, attributes):
        method_attribute_access = defaultdict(set)
        for method in methods:
            for node in ast.walk(method):
                if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id == "self":
                    method_attribute_access[method.name].add(node.attr)

        shared_pairs = 0
        for m1, attrs1 in method_attribute_access.items():
            for m2, attrs2 in method_attribute_access.items():
                if m1 != m2 and attrs1 & attrs2:
                    shared_pairs += 1

        num_methods = len(methods)
        max_pairs = num_methods * (num_methods - 1) // 2
        return shared_pairs / max_pairs if max_pairs > 0 else 0

    def calculate_atfd(self, methods, class_name):
        foreign_accesses = set()
        for method in methods:
            for node in ast.walk(method):
                if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
                    if node.value.id != "self":
                        foreign_accesses.add((node.value.id, node.attr))
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id != "self":
                        foreign_accesses.add((node.func.value.id, node.func.attr))
        return len(foreign_accesses)

    def detect_god_classes(self, wmc_threshold=41, tcc_threshold=1 / 3, atfd_threshold=5):
        god_classes = []
        for class_name, metrics in self.classes.items():
            if metrics["wmc"] >= wmc_threshold and metrics["tcc"] < tcc_threshold and metrics["atfd"] > atfd_threshold:
                god_classes.append((class_name, metrics))
        return god_classes