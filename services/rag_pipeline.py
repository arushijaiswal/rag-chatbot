from services.retriever import get_relevant_docs
from services.generator import generate_answer

def get_rag_response(question: str) -> str:
    """
    Retrieves relevant documents and generates an answer using LLM.
    """
    # Step 1: Retrieve relevant documents
    docs = get_relevant_docs(question)

    # Step 2: Generate answer based on retrieved docs
    answer = generate_answer(question, docs)
    return answer
# rag_pipeline.py - RAG pipeline for processing user queries
# This file contains the logic for retrieving relevant documents and generating answers using LLM