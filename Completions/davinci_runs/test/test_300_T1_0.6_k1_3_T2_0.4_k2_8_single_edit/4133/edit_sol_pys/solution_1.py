#!/bin/bash

# This script allows you to run the server without having to install it.
# It will create a virtual environment, install the dependencies and run the server.
# You can also use it to run the server after you install it.

# Create the virtual environment
virtualenv env

# Activate the virtual environment
source env/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Run the server
python app.py
