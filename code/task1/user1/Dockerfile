# Use a base image with Python installed
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the client-side code into the container
COPY user1_client.html /app

# Expose port 8000 for the WebSocket server
EXPOSE 8000

# Run a simple HTTP server to serve the HTML file
CMD ["python", "-m", "http.server", "8000"]
