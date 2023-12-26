# Dockerfile

# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the FastAPI dependencies
RUN pip install -r requirements.txt

# Copy the main.py file
COPY . /app

# Expose the port that FastAPI will run on 
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
