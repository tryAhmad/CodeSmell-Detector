# Code Smell Detection Project

This project is designed to detect common code smells such as Long Methods, God Classes, Long Parameter Lists, and Large Classes. It uses a Flask backend to provide APIs for code analysis and a React frontend for a user-friendly interface.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Project Description

This tool identifies code smells in software projects. The backend is implemented using Flask and provides APIs for analyzing code. The frontend, built with React, interacts with these APIs to display results in an intuitive manner.

The four code smells addressed are:
- **Long Methods** - Functions that are excessively long.
- **God Class** - Classes that handle too many responsibilities.
- **Long Parameter List** - Functions with too many parameters.
- **Large Class** - Classes with too many methods and attributes.

The backend processes input code, detects these issues, and returns results via API endpoints. The frontend visualizes the findings for users.

## Technologies Used

**Backend (Flask):**
- Flask (Python web framework)
- Flask-CORS (for cross-origin requests)
- AST (Abstract Syntax Tree for Python code analysis)
- JSON (for storing analysis results)

**Frontend (React):**
- React (UI framework)
- Fetch API (for API communication)
- React Toastify (for notifications)
- CSS (for styling)


## Installation and Setup

Follow these steps to set up and run the project locally:

### 1. Prerequisites

Ensure you have the following installed:
- Python (3.8 or above)
- Node.js and npm
- Flask

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```
Install the required Python packages:

```bash
pip install flask flask-cors
```
Run the Flask server:

```bash
python main.py
```
The API will be available at http://127.0.0.1:5000.

### 3. Frontend Setup
Navigate to the frontend directory:

```bash
cd frontend
```

The frontend will be available at http://localhost:3000.

API Endpoints
Below is the endpoint exposed by the Flask backend:

Method	Endpoint	Description
POST	/analyze-folder	Analyzes Python code for code smells

## Usage
1. Start the Flask backend server.
2. Start the React frontend application.
3. Enter the folder path containing your Python code into the input box.
4. Click on the Analyze button to start the analysis.
5. View the detected code smells displayed in a structured format.
6. Results will also be saved in the backend/analysis_results.json file

## API Endpoints
Below is the endpoint exposed by the Flask backend:

| Method | Endpoint        | Description                          |
|--------|-----------------|--------------------------------------|
| POST   | /analyze-folder | Analyzes Python code for code smells |

## Contact
For any questions or suggestions, contact:

Name: [Muhammad Ahmad]
Email: [ahmadsaeed3220@gmail.com]
