#!/bin/bash

# Define the virtual environment name
venv_name="myenv"

# Step 1: Create and activate the virtual environment
python3 -m venv $venv_name
source $venv_name/bin/activate

# Step 2: Install dependencies from requirements.txt
# pip install -r requirements.txt
pip install flask
pip install git+https://github.com/newrelic/newrelic-python-agent@8e17a97c8e4e869a8af200d65727a70b0a10d568
pip install git+https://github.com/newrelic/nr-openai-observability@staging

# Step 3: Run the Flask app
#Validate newrelic.ini
newrelic-admin validate-config newrelic.ini

NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python app.py