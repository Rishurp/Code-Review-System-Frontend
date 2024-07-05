import joblib
import os
import pandas as pd
from src.data_preprocessing import preprocess_text

def load_model_and_vectorizer():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'vectorizer.pkl')

    print(f"Loading model from {model_path}")
    model = joblib.load(model_path)
    print("Model loaded successfully")

    print(f"Loading vectorizer from {vectorizer_path}")
    vectorizer = joblib.load(vectorizer_path)
    print("Vectorizer loaded successfully")
    
    return model, vectorizer

def load_csv_data():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_code_feedback_js.csv')
    data = pd.read_csv(csv_path)
    return data

data = load_csv_data()

def normalize_code(code):
    # Normalize by removing leading/trailing whitespaces and redundant spaces/newlines
    return ' '.join(code.split())

def get_feedback_from_csv(code_snippet):
    feedback = []
    normalized_code_snippet = normalize_code(code_snippet)
    print(f"Normalized code snippet to match:\n{normalized_code_snippet}")
    for index, row in data.iterrows():
        normalized_csv_snippet = normalize_code(row['code_snippet'])
        print(f"Checking normalized row code snippet:\n{normalized_csv_snippet}")
        if normalized_csv_snippet == normalized_code_snippet:
            print(f"Match found! Annotation: {row['annotations']}")
            if pd.notna(row['annotations']):
                feedback.append(row['annotations'])
    print(f"Feedback collected: {feedback}")
    return feedback

def analyze_code(code_snippet):
    model, vectorizer = load_model_and_vectorizer()
    processed_code = preprocess_text(code_snippet)
    features = vectorizer.transform([processed_code])
    prediction = model.predict(features)
    
    feedback = get_feedback_from_csv(code_snippet)
    
    result = 'correct' if prediction == 1 else 'incorrect'
    
    return result, feedback
