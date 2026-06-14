# Dockerfile for the backend

# Start with a base image
FROM python:3.12-slim

# Expose the port
EXPOSE 5000

# Set the working directory
# Can be any directory, but /app is a common convention
WORKDIR /app

# Copy package files to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend files to the working directory
COPY . .

# Run the application
CMD ["python", "main.py"]

# Order for the above layers can be changed
# However, put every layer that won't change often at the top
# This will help with caching and speed up build times
