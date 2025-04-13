from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv("key.env")

app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def get_fertilizer_prediction(soil_data):
    prompt = f"""
    Given the following soil data: {soil_data}, predict the best fertilizer and provide a short explanation.

    Provide the output in the following format:
    Fertilizer: [Fertilizer Name]
    Explanation: [Explanation]
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def index():
    return render_template("4th.html")

@app.route('/predict', methods=['POST'])
def predict():
    soil_data = request.form['soil_data']
    prediction = get_fertilizer_prediction(soil_data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)