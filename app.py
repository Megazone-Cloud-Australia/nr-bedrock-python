import os
import boto3
import json

# Import the Flask module
from flask import Flask, request
from nr_openai_observability import monitor

# Replace 'NEW_RELIC_LICENSE_KEY' with the actual name of your environment variable
env_variable_name = 'NEW_RELIC_LICENSE_KEY'

# Check if the environment variable exists
if env_variable_name in os.environ:
    # Print the value of the environment variable
    print(f"{env_variable_name}: {os.environ[env_variable_name]}")
else:
    print(f"{env_variable_name} not found in environment variables.")

monitor.initialization(
    application_name="Python AWS Bedrock Server"
)

bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1') # Use bedrock from US-EAST-1 as not available in Syd

# Create a Flask web application
app = Flask(__name__)

# Define the root endpoint
@app.route('/')
def hello():
    return 'Hello world'

# POST endpoint at the root
@app.route('/', methods=['POST'])
def prompt():
    data = request.json  # Assuming the incoming data is in JSON format
    body = json.dumps({
        "prompt": data['prompt'], 
        "maxTokens": 200,
        "temperature": 0.5,
        "topP": 0.5
    })

    modelId = 'ai21.j2-mid-v1'
    accept = 'application/json'
    contentType = 'application/json'

    response = bedrock_client.invoke_model(
        body=body, 
        modelId=modelId, 
        accept=accept, 
        contentType=contentType
    )

    response_body = json.loads(response.get('body').read())

    # text
    response_text = response_body.get('completions')[0].get('data').get('text')
    print(response_text)
    return response_text

# Run the application if this script is executed
if __name__ == '__main__':
    # Run the app on port 80
    app.run(host='0.0.0.0', port=80)