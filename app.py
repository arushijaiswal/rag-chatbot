from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your RAG pipeline
from services.rag_pipeline import get_rag_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    if not question:
        return jsonify({'answer': 'No question provided.'})

    # Get answer from RAG pipeline
    answer = get_rag_response(question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)

# app.py - Flask application for RAG chatbot
# This file sets up the Flask app, loads environment variables, and defines routes for the chatbot