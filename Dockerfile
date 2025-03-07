# Use a lightweight base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY app.py .

# Install dependencies (if needed)
RUN pip install flask requests

# Run the script
CMD ["python", "app.py"]
