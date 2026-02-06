# backend/chat.py

import joblib
import os
from preprocess import clean_text
import pandas as pd
import random

# =======================
# Paths
# =======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model/assistant_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")
DATA_PATH = os.path.join(BASE_DIR, "../data/intents.csv")

# =======================
# Load dataset
# =======================
df = pd.read_csv(DATA_PATH)

# =======================
# Load trained model & vectorizer
# =======================
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# =======================
# Helper function to get response
# =======================
def get_response(intent):
    responses = df[df['intent'] == intent]['response'].tolist()
    if responses:
        response
