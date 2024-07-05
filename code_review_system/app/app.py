import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template
from src.feedback import analyze_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code_snippet = request.form['code_snippet']
    result, feedback = analyze_code(code_snippet)
    return render_template('index.html', result=result, feedback=feedback, code_snippet=code_snippet)

@app.route('/submit_new_problem', methods=['POST'])
def submit_new_problem():
    new_code_snippet = request.form['new_code_snippet']
    expected_result = request.form['expected_result']
    annotation = request.form['annotation']
    
    # Append new data to CSV
    new_data = pd.DataFrame([[new_code_snippet, expected_result, annotation]], 
                            columns=['code_snippet', 'correctness', 'annotations'])
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_code_feedback_js.csv')
    new_data.to_csv(csv_path, mode='a', header=False, index=False)
    
    return render_template('index.html', message="New problem submitted successfully!")

if __name__ == '__main__':
    app.run(debug=True)
