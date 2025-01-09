import os
from flask import Flask, request, jsonify
from googleapiclient.discovery import build
from google.oauth2 import service_account
import sqlite3
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes
    (id INTEGER PRIMARY KEY, ingredients TEXT, recipe TEXT)
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

# Create credentials
creds = None
if creds is None or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        creds = service_account.Credentials.from_service_account_file(
            'credentials.json', scopes=['https://www.googleapis.com/auth/cloud-platform']
        )

# Create the client
client = build('gemini', 'v2', credentials=creds)

@app.route('/recipes', methods=['POST'])
def get_recipe():
    data = request.get_json()
    ingredients = data['ingredients']

    # Connect to SQLite database
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    # Check if recipe exists in database
    cursor.execute('SELECT recipe FROM recipes WHERE ingredients = ?', (ingredients,))
    row = cursor.fetchone()

    if row:
        return jsonify({'recipe': row[0]})

    # Call the Gemini API
    response = client.projects().locations().models().generateText(
        parent=f'projects/{os.getenv("GEMINI_API_PROJECT")}/locations/{os.getenv("GEMINI_API_LOCATION")}/models/gemini-2-0-flash-exp',
        body={
            'prompt': f'Generate a recipe using the following ingredients: {ingredients}',
            'maxTokens': 512,
            'temperature': 0.7,
            'topP': 0.9,
            'numReturnSequences': 1
        }
    ).execute()

    # Get the generated recipe
    recipe = response['sequences'][0]['text']

    # Save the recipe to the database
    cursor.execute('INSERT INTO recipes (ingredients, recipe) VALUES (?, ?)', (ingredients, recipe))
    conn.commit()

    # Close the connection
    conn.close()

    return jsonify({'recipe': recipe})

if __name__ == '__main__':
    app.run(debug=True)