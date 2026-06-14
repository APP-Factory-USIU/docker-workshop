# Dockerfile for the frontend service

# Must always start with a base image
FROM nginx:alpine

# Copy the frontend files to the nginx html directory
# This path may be different depending on the frontend framework
# Consult the frontend framework documentation for the correct path
COPY . /usr/share/nginx/html
