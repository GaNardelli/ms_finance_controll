# MS Finance Control

This is a Flask application for managing finances.  It provides a basic API for interacting with income data.

## Getting Started

To run the application:

1.  **Build the Docker image:**
    ```bash
    docker build -t ms_finance_control .
    ```
2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 ms_finance_control
    ```

## Running Without Docker

To run the application directly on your system, you need to have Python and the required packages installed.

1.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    flask --app app.py --debug run --host=0.0.0.0
    ```