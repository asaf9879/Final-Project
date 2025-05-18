# Flask Web Application

This is a simple Flask web application that serves a static HTML page (`index.html`) using a Python backend (`app.py`). The application is containerized using Docker and orchestrated with Docker Compose.

## 📁 Project Structure

├── app.py
├── templates/
│ └── index.html
├── Dockerfile
├── docker-compose.yml
└── README.md



## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 🔧 Running the Application

1. **Build and Start the Application**

   ```bash
   docker-compose up --build


Docker Compose Overview
The docker-compose.yml file defines a single service:

web: Builds the image from the Dockerfile, maps port 5000, and runs the Flask application.

📝 File Descriptions
app.py: Main Flask application script.

index.html: HTML page rendered by the Flask app, located in the templates/ directory.

Dockerfile: Builds the Flask app image.

docker-compose.yml: Defines the services and configuration to run the app in containers.
