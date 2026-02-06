# backend/app.py

from flask import Flask, render_template, request, jsonify
import os
import joblib
import pandas as pd
import random
from preprocess import clean_text
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    app.run()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model/assistant_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")
DATA_PATH = os.path.join(BASE_DIR, "../data/intents.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Load trained model & vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

app = Flask(__name__, template_folder="frontend", static_folder="frontend")

def get_response(intent):
    responses = df[df['intent'] == intent]['response'].tolist()
    if responses:
        response = random.choice(responses)
        if response.startswith("http"):
            response = f"<a href='{response}' target='_blank'>{response}</a>"
        return response
    return "I'm still learning  Can you rephrase that?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def respond():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "Please type something."})

    clean_input = clean_text(user_input)
    vec_input = vectorizer.transform([clean_input])
    intent_pred = model.predict(vec_input)[0]
    response = get_response(intent_pred)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

