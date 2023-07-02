# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the deployment script and the model file to the container
COPY deployment_script.py .
COPY model.pkl .
COPY preprocessor.pkl .
# Install the required dependencies
RUN pip install flask joblib

# Expose the port number the Flask app runs on
#EXPOSE 8000

RUN pip install -r requirements.txt
# Set the entrypoint command to run the deployment script
CMD ["python", "deployment_script.py"]
