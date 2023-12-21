#!/bin/bash

# Define the virtual environment name
venv_name="myenv"

# Step 1: Create and activate the virtual environment
python3 -m venv $venv_name
source $venv_name/bin/activate

# Step 2: Install dependencies from requirements.txt
pip install -r requirements.txt

# Step 3: Run the Flask app
#Validate newrelic.ini
newrelic-admin validate-config newrelic.ini

NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python app.py