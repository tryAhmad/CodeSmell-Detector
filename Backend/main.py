import os
import ast
import json
from flask_cors import CORS
from flask import Flask, request, jsonify
from godClass import GodClassDetector
from longMethod import detect_long_methods
from largeClass import detect_large_classes
from longPram import detect_long_parameter_list

app = Flask(__name__)
CORS(app)

@app.route('/analyze-folder', methods=['POST'])
def analyze_folder():
    data = request.json
    folder_path = data.get('folderPath')

    if not folder_path or not os.path.isdir(folder_path):
        return jsonify({"error": "Invalid folder path"}), 400

    results = {
        "long_parameter_list": [],
        "long_methods": [],
        "god_classes": [],
        "large_classes": []
    }

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()

                # Long Parameter List
                long_params = detect_long_parameter_list(code)
                if long_params:
                    results["long_parameter_list"].append({"file": file, "issues": long_params})

                # Long Methods
                long_methods = detect_long_methods(code)
                if long_methods:
                    results["long_methods"].append({"file": file, "issues": long_methods})

                # God Classes
                god_class_detector = GodClassDetector(code)
                tree = ast.parse(code)
                god_class_detector.visit(tree)
                god_classes = god_class_detector.detect_god_classes()
                if god_classes:
                    for class_name, metrics in god_classes:
                        results["god_classes"].append({
                            "file": file,
                            "class_name": class_name,
                            "wmc": metrics["wmc"],
                            "tcc": metrics["tcc"],
                            "atfd": metrics["atfd"]
                        })

                # Large Classes
                large_classes = detect_large_classes(code)
                if large_classes:
                    results["large_classes"].append({"file": file, "issues": large_classes})

    # Save results to a JSON file
    output_file = "analysis_results.json"
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, indent=4)

    # Return the results as a JSON response
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)