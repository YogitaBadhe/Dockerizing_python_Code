# Dockerizing Python Code for Tic-Tac-Toe Game

This project demonstrates how to Dockerize a simple Python-based Tic-Tac-Toe game. By the end of this guide, you'll have a containerized Python application that you can run anywhere using Docker.

## Clone Repo
To get started, clone the repository and navigate into the project folder:
```bash
git clone https://github.com/YogitaBadhe/Dockerizing_python_Code.git
cd Dockerizing_python_Code
```

## Prerequisites

Before you begin, ensure that you have the following installed:

### 1. **Docker**
Ensure that Docker is installed on your system. If not, you can install Docker using the following command:
```bash
sudo yum install docker -y
```

### 2. **Git**
You need Git to clone the repository. If you don't have Git installed, use:
```bash
sudo yum install git -y
```

### 3. **Python**
You will need Python installed to test the Tic-Tac-Toe game. Install Python if it's not already on your system:
```bash
sudo yum install python -y
```

## Steps to Dockerize Python Code

### 1. **Setup Docker**
Start the Docker service and enable it to start on boot:
```bash
sudo systemctl start docker
sudo systemctl enable docker
```
Verify your Docker installation:
```bash
docker --version
```

### 2. **Configure Git**
Configure your Git user details (optional but recommended):
```bash
git config --global user.name "YogitaBadhe"
git config --global user.email "ybadhe0990@gmail.com"
```

### 3. **Create and Test Python Script**
Create the Python script for your Tic-Tac-Toe game:
```bash
sudo touch tic-tac-toe.py
sudo nano tic-tac-toe.py
```

Paste your Python code into the file, then test it locally:
```bash
python3 tic-tac-toe.py
```

### 4. **Create Dockerfile**
Create a `Dockerfile` in the root of your project directory:
```bash
touch Dockerfile
sudo nano Dockerfile
```

Add the following content to the `Dockerfile`:
```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages (in this case, there are none)
RUN pip install --no-cache-dir

# Run tic-tac-toe.py when the container launches
CMD ["python", "tic-tac-toe.py"]
```

### 5. **Build and Push Docker Image**

1. **Log in to Docker Hub (if you haven’t already):**
   ```bash
   sudo docker login
   ```

2. **Build the Docker image**:
   ```bash
   sudo docker build -t ybadhe/pythonproject .
   ```

3. **Verify the Docker image is built**:
   ```bash
   sudo docker images
   ```

4. **Push the Docker image to Docker Hub**:
   ```bash
   sudo docker push ybadhe/pythonproject
   ```

### 6. **Run Docker Container**

1. **Run your Docker container**:
   ```bash
   sudo docker run ybadhe/pythonproject
   ```

2. **List all running Docker containers**:
   ```bash
   sudo docker ps -a
   ```

---

## Interacting with the Game

Once the container is running, you'll interact with the Tic-Tac-Toe game through the terminal. The game will prompt you to enter row and column numbers for player moves (e.g., `0 1` for row 0, column 1).

### Sample Gameplay:
```
Tic-Tac-Toe Game
| X |   |   |
---------
|   | O |   |
---------
|   |   | X |
Player X, enter row and column (0-2): 1 1
Player O, enter row and column (0-2): 0 0
...
```

### 7. **Stopping the Docker Container**
To stop the container, use the following command:
```bash
sudo docker stop <container_id>
```
You can get the `<container_id>` by running:
```bash
sudo docker ps -a
```

---

## Conclusion

By following these steps, you have successfully Dockerized a Python Tic-Tac-Toe game. You can now run the game as a Docker container on any machine that supports Docker.

If you encounter any issues, please open an issue on the repository, and I'll assist you as soon as possible.

---

This README provides clear instructions for setting up, Dockerizing, and running the Python Tic-Tac-Toe game.
