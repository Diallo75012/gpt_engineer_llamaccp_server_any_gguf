#!/bin/bash

# Install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the Flask app
python app.py
