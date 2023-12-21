# Import the Flask module
from flask import Flask, request

# Create a Flask web application
app = Flask(__name__)

# Define the root endpoint
@app.route('/')
def hello():
    return 'Hello, World!'

# POST endpoint at the root
@app.route('/', methods=['POST'])
def post_example():
    data = request.json  # Assuming the incoming data is in JSON format
    return f'Received POST request with data: {data}'

# Run the application if this script is executed
if __name__ == '__main__':
    # Run the app on port 80
    app.run(host='0.0.0.0', port=80)