import os
from flask import Flask, request, render_template
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        api_key = os.getenv('API_KEY')
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        response_recipe = model.generate_content(f"Create a recipe using {ingredient}")
        response_image = model.generate_content(f"Create an image of a dish made with {ingredient}")
        return render_template('result.html', recipe=response_recipe.text, image=response_image.text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()