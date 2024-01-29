import json
from flask import Flask, request
from flask_cors import CORS

import boto3
import newrelic.agent
from nr_openai_observability import monitor

newrelic.agent.initialize("newrelic.ini")
monitor.initialization()

bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1') # Use bedrock from US-EAST-1 as not available in Syd

# Create a Flask web application
app = Flask(__name__)
CORS(app)

# Define the root endpoint
@app.route('/')
def hello():
    return 'Hello world'

# POST endpoint at the root
@app.route('/', methods=['POST'])
def prompt():
    data = request.json  # Assuming the incoming data is in JSON format


    accept = 'application/json'
    contentType = 'application/json'

    modelId = data.get('modelId', 'ai21.j2-mid-v1') #meta.llama2-13b-chat-v1

    if modelId == 'meta.llama2-13b-chat-v1':
        body = json.dumps({
            "prompt": data['prompt'], 
            "max_gen_len": 200,
            "temperature": 0.5,
            "top_p": 0.5,
        })

        response = bedrock_client.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

        response_body = json.loads(response.get('body').read())
        response_text = response_body.get('generation')

    else:
        body = json.dumps({
            "prompt": data['prompt'], 
            "maxTokens": 200,  # Default maxTokens for other modelIds
            "temperature": 0.5,
            "topP": 0.5
        })

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