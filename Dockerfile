# Use the official Python image from the Docker Hub
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variables
# PYTHONUNBUFFERED: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONDONTWRITEBYTECODE: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to have it mapped by Docker daemon
EXPOSE 8000

# Define the start command to run your app using gunicorn
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
