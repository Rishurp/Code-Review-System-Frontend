import joblib
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, vectorizer, data):
    X = vectorizer.transform(data['code_snippet'])
    y = data['correctness'].map({'correct': 1, 'incorrect': 0})
    
    y_pred = model.predict(X)
    
    print("Accuracy:", accuracy_score(y, y_pred))
    print("Classification Report:\n", classification_report(y, y_pred))
