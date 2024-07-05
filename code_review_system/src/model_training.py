import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    # Load preprocessed data
    data = pd.read_csv('../data/sample_code_feedback_js.csv')

    # Convert text data to TF-IDF features
    vectorizer = TfidfVectorizer(max_features=500)
    X = vectorizer.fit_transform(data['code_snippet'])
    y = data['correctness'].map({'correct': 1, 'incorrect': 0})

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Define file paths
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'vectorizer.pkl')

    # Save model and vectorizer
    print(f"Saving model to {model_path}")
    joblib.dump(model, model_path)
    print(f"Saving vectorizer to {vectorizer_path}")
    joblib.dump(vectorizer, vectorizer_path)
    print("Model and vectorizer saved successfully")

if __name__ == "__main__":
    train_model()
