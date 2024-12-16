import ast

def detect_long_parameter_list(file_content, threshold=7):
    tree = ast.parse(file_content)
    results = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            num_params = len(node.args.args) + len(node.args.kwonlyargs)
            if node.args.vararg:
                num_params += 1
            if node.args.kwarg:
                num_params += 1
            
            if num_params > threshold:
                results.append({
                    "function_name": node.name,
                    "line_number": node.lineno,
                    "parameter_count": num_params,
                    "threshold": threshold
                })

    return results