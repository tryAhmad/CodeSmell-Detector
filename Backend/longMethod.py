import ast

def detect_long_methods(file_content, line_limit=10):
    import ast
    
    tree = ast.parse(file_content)
    results = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Get the start line of the function
            start_line = node.lineno
            
            # Calculate the end line manually
            end_line = max(
                (child.lineno for child in ast.walk(node) if hasattr(child, 'lineno')),
                default=start_line
            )
            method_lines = end_line - start_line + 1

            if method_lines > line_limit:
                results.append({
                    "function_name": node.name,
                    "start_line": start_line,
                    "end_line": end_line,
                    "line_count": method_lines,
                    "threshold": line_limit
                })

    return results