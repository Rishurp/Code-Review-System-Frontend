# src/data_preprocessing.py

import pandas as pd
import nltk
from nltk.corpus import stopwords

def download_nltk_resources():
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

download_nltk_resources()

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = text.lower().split()
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data['code_snippet'] = data['code_snippet'].apply(preprocess_text)
    return data









