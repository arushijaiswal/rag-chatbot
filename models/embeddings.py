from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding(text: str, model: str = "text-embedding-3-small"):
    """
    Generate embedding for a given text using OpenAI.
    """
    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding
# embeddings.py - Embedding generation for RAG pipeline
# This file contains the logic for generating embeddings using OpenAI's API