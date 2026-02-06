# backend/train.py

import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from preprocess import clean_text

# =======================
# Paths
# =======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/intents.csv")
MODEL_DIR = os.path.join(BASE_DIR, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "assistant_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

# Create model directory if not exists
os.makedirs(MODEL_DIR, exist_ok=True)

# =======================
# Load dataset
# =======================
df = pd.read_csv(DATA_PATH)

# Make sure the CSV has required columns
required_columns = ["text", "intent", "response"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' is missing in CSV file!")

# =======================
# Preprocess text
# =======================
df['clean_text'] = df['text'].apply(clean_text)

# =======================
# Vectorization
# =======================
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['clean_text'])
y = df['intent']

# =======================
# Train model
# =======================
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# =======================
# Save model and vectorizer
# =======================
joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)

print(" Model and vectorizer have been trained and saved successfully!")
print(f"Model saved at: {MODEL_PATH}")
print(f"Vectorizer saved at: {VECTORIZER_PATH}")
