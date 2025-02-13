FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt


# Copy the entire app directory into the container
COPY . .

# Set environment variables
ENV FLASK_APP=app.py


# Expose the Flask port
EXPOSE 5000

# Run the app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]

