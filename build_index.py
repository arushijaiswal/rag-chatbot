# build_index.py
import os
from services.embeddings_service import save_faiss_index
from models.embeddings import get_embedding
import faiss
import numpy as np

# Paths
DOCS_DIR = "data/sample_docs"
INDEX_PATH = "data/embeddings_store/faiss_index.index"

def build_index():
    documents = []
    for fname in os.listdir(DOCS_DIR):
        if fname.endswith(".txt"):
            with open(os.path.join(DOCS_DIR, fname), "r", encoding="utf-8") as f:
                documents.append(f.read())

    print(f"Loaded {len(documents)} documents.")

    embeddings = [get_embedding(doc) for doc in documents]
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    save_faiss_index(index)
    print(f"FAISS index saved to {INDEX_PATH}")

if __name__ == "__main__":
    build_index()
# build_index.py - Build FAISS index for RAG pipeline
# This script reads documents, generates embeddings, and saves them in a FAISS index