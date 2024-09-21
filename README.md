
# Flask To-Do List App

This is a simple **Flask-based To-Do List application** where users can add and delete tasks. It uses Flask for the backend and renders tasks dynamically on the frontend using HTML templates.

## Features
- Add new tasks to the to-do list.
- Delete tasks from the list.

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Flask**: Flask will be installed using `pip` through `requirements.txt`.

### Installation

1. **Clone the repository**:

   Open your terminal or Command Prompt and clone the repository by running:
   ```bash
   git clone https://github.com/your-username/flask-todo-app.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd flask-todo-app
   ```

3. **Set up a virtual environment**:

   It is recommended to use a virtual environment to manage dependencies.

   - On Windows:
     ```bash
     python -m venv venv
     ```
   - On MacOS/Linux:
     ```bash
     python3 -m venv venv
     ```

4. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:

   Install the required dependencies (Flask) using `pip` from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. **Run the Flask application**:

   After setting up everything, run the Flask app:
   ```bash
   python app/app.py
   ```

2. **View the app in your browser**:

   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

   You should now be able to view the to-do list app where you can add and delete tasks.

### Directory Structure

Here’s the structure of the project:

```
flask-todo-app/
├── app/
│   └── app.py           # Flask application code
├── templates/
│   └── index.html       # HTML template for the app
├── venv/                # Virtual environment (created after setup)
├── Dockerfile           # Docker configuration file (if needed)
├── requirements.txt     # Python dependencies
└── README.md            # This README file
```

### Docker Support (Optional)

You can also run this project using Docker. Here’s how:

1. **Build the Docker image**:
   ```bash
   docker build -t flask-todo-app .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 flask-todo-app
   ```

3. **Access the app** at:
   ```
   http://localhost:5000
   ```
