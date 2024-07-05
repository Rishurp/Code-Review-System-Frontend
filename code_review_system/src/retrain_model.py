# src/retrain_model.py

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_code_feedback_js.csv')
    data = pd.read_csv(csv_path)
    return data

def preprocess_text(text):
    return ' '.join(text.split())

def train_model():
    data = load_data()
    data['processed_code'] = data['code_snippet'].apply(preprocess_text)
    X = data['processed_code']
    y = data['correctness'].apply(lambda x: 1 if x == 'correct' else 0)
    
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)
    
    model = LogisticRegression()
    model.fit(X_vec, y)
    
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'vectorizer.pkl')
    
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    
    print("Model and vectorizer retrained and saved successfully.")

if __name__ == '__main__':
    train_model()
