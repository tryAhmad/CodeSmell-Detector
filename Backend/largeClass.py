import ast

class LargeClassDetector(ast.NodeVisitor):
    def __init__(self, nloc_threshold=1000):
        self.nloc_threshold = nloc_threshold
        self.large_classes = []

    def visit_ClassDef(self, node):
        class_start = node.lineno
        class_end = max((child.lineno for child in ast.walk(node) if hasattr(child, 'lineno')), default=class_start)
        nloc = class_end - class_start + 1

        if nloc > self.nloc_threshold:
            self.large_classes.append({
                'class_name': node.name,
                'nloc': nloc,
                'start_line': class_start,
                'end_line': class_end
            })

        self.generic_visit(node)

def detect_large_classes(file_content, nloc_threshold=1000):
    tree = ast.parse(file_content)
    detector = LargeClassDetector(nloc_threshold)
    detector.visit(tree)
    return detector.large_classes