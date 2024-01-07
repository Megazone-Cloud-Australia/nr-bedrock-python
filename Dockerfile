# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
RUN pip install flask-cors
RUN pip install git+https://github.com/newrelic/newrelic-python-agent@8e17a97c8e4e869a8af200d65727a70b0a10d568
RUN pip install git+https://github.com/newrelic/nr-openai-observability@staging
RUN pip install boto3
RUN pip install newrelic
# Make port 443 available to the world outside this container
EXPOSE 443


# Run app.py when the container launches
RUN newrelic-admin validate-config newrelic.ini

CMD ["sh", "-c", "NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python app.py"]
