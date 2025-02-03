# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run tic-tac-toe.py when the container launches
CMD ["python", "tic-tac-toe.py"]

