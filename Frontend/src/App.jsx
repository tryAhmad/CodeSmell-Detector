import React, { useState } from "react";
import { toast } from "react-toastify";
import "./App.css";

const App = () => {
  const [folderPath, setFolderPath] = useState("");
  const [results, setResults] = useState(null);
  const [error, setError] = useState("");

  const handleInputChange = (e) => {
    setFolderPath(e.target.value);
  };

  const analyzeFolder = async () => {
    if (!folderPath) {
      toast.error("Please enter a valid folder path.");
      return;
    }

    try {
      setError("");
      const response = await fetch("http://127.0.0.1:5000/analyze-folder", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ folderPath }),
      });

      if (!response.ok) {
        const errorResponse = await response.json();
        toast.error(
          errorResponse.error || "An error occurred while analyzing the folder."
        );
        return;
      }

      const data = await response.json();
      toast.success("Results Saved in JSON file");
      setResults(data);
    } catch (err) {
      toast.error("An error occurred while communicating with the server.");
    }
  };

  const totalLongParameterSmells = results?.long_parameter_list?.reduce(
    (total, file) => total + file.issues.length,
    0
  );

  const renderResults = () => {
    if (!results) return null;

    return (
      <div>
        <h2>Analysis Results:</h2>
        <div className="results-container">
          {/* Long Methods */}
          {results.long_methods?.length > 0 && (
            <div className="result-card">
              <h3>Long Methods</h3>
              <strong>Code Smells Detected:</strong>{" "}
              {results.long_methods.reduce(
                (total, file) => total + file.issues.length,
                0
              ) || "0"}
              <ul>
                {results.long_methods.map((file, fileIndex) => (
                  <li key={fileIndex}>
                    <strong>File:</strong> {file.file}
                    <ul>
                      {file.issues.map((method, index) => (
                        <li key={index}>
                          <strong>Function:</strong> {method.function_name}
                          <ul>
                            <li>
                              <strong>Start Line:</strong> {method.start_line}
                            </li>
                            <li>
                              <strong>End Line:</strong> {method.end_line}
                            </li>
                            <li>
                              <strong>Total Lines:</strong> {method.line_count}
                            </li>
                            <li>
                              <strong>Threshold:</strong> {method.threshold}
                            </li>
                            <br />
                          </ul>
                        </li>
                      ))}
                    </ul>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* God Classes */}
          {results.god_classes?.length > 0 && (
            <div className="result-card">
              <h3>God Classes</h3>
              <strong>Code Smells Detected:</strong>{" "}
              {results.god_classes.length || "0"}
              <ul>
                {results.god_classes.map((cls, index) => (
                  <li key={index}>
                    <strong>File:</strong> {cls.file}
                    <ul>
                      <li>
                        <strong>Class Name:</strong> {cls.class_name}
                      </li>
                      <li>
                        <strong>WMC:</strong> {cls.wmc}
                      </li>
                      <li>
                        <strong>TCC:</strong> {cls.tcc.toFixed(2) || "N/A"}
                      </li>
                      <li>
                        <strong>ATFD:</strong> {cls.atfd}
                      </li>
                      <br />
                    </ul>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Large Classes */}
          {results.large_classes?.length > 0 && (
            <div className="result-card">
              <h3>Large Classes</h3>
              <strong>Code Smells Detected:</strong>{" "}
              {results.large_classes.reduce(
                (total, file) => total + file.issues.length,
                0
              ) || "0"}
              <ul>
                {results.large_classes.map((file, fileIndex) => (
                  <li key={fileIndex}>
                    <strong>File:</strong> {file.file}
                    <ul>
                      {file.issues.map((cls, index) => (
                        <li key={index}>
                          <strong>Class:</strong> {cls.class_name}
                          <ul>
                            <li>
                              <strong>Lines of Code:</strong> {cls.nloc}
                            </li>
                            <li>
                              <strong>Start Line:</strong> {cls.start_line}
                            </li>
                            <li>
                              <strong>End Line:</strong> {cls.end_line}
                            </li>
                            <br />
                          </ul>
                        </li>
                      ))}
                    </ul>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Functions with Long Parameter Lists */}
          {results?.long_parameter_list?.length > 0 && (
            <div className="result-card">
              <h3>Functions with Long Parameter Lists</h3>
              <strong>Code Smells Detected:</strong>{" "}
              {totalLongParameterSmells || "0"}
              <ul>
                {results.long_parameter_list.map((file, fileIndex) => (
                  <li key={fileIndex}>
                    <strong>File:</strong> {file.file}
                    <ul>
                      {file.issues.map((func, index) => (
                        <li key={index}>
                          <strong>Function:</strong> {func.function_name}
                          <ul>
                            <li>
                              <strong>Line Number:</strong> {func.line_number}
                            </li>
                            <li>
                              <strong>Parameter Count:</strong>{" "}
                              {func.parameter_count}
                            </li>
                            <li>
                              <strong>Threshold:</strong> {func.threshold}
                            </li>
                            <br />
                          </ul>
                        </li>
                      ))}
                    </ul>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* No Results Found */}
          {results.long_methods?.length === 0 &&
            results.god_classes?.length === 0 &&
            results.large_classes?.length === 0 &&
            results.long_parameter_list?.length === 0 && (
              <p>No code smells detected!</p>
            )}
        </div>
      </div>
    );
  };

  return (
    <div
      className="analyzer-box"
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
        color: "black",
        textAlign: "center",
        boxShadow: "0 4px 8px rgba(214, 188, 188, 0.75)",
        borderRadius: "20px",
        backgroundColor: "lightgrey",
      }}
    >
      <h1 style={{ fontFamily: "fantasy", color: "#3d3c3c" }}>
        Code Smell Analyzer
      </h1>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          marginBottom: "20px",
        }}
      >
        <label
          htmlFor="folderPath"
          style={{ color: "black", fontFamily: "fantasy" }}
        >
          Enter Folder Path:
        </label>
        <input
          type="text"
          id="folderPath"
          value={folderPath}
          onChange={handleInputChange}
          style={{
            marginLeft: "10px",
            padding: "5px",
            width: "610px",
            color: "black",
            backgroundColor: "white",
            border: "none",
            borderRadius: "8px",
          }}
        />
      </div>
      <button
        onClick={analyzeFolder}
        style={{
          padding: "10px 20px",
          backgroundColor: "#007BFF",
          color: "white",
          border: "none",
          cursor: "pointer",
        }}
      >
        Analyze
      </button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {renderResults()}
    </div>
  );
};

export default App;
