import faiss
import pickle
import numpy as np
import os
from models.embeddings import get_embedding

INDEX_PATH = "data/embeddings_store/faiss_index.index"
META_PATH = "data/embeddings_store/metadata.pkl"

def get_relevant_docs(query: str, top_k: int = 3):
    """
    Retrieves top-k relevant documents from FAISS index.
    """
    # ⚠️ This is the fix: The check and loading are now inside the function.
    if not os.path.exists(INDEX_PATH) or not os.path.exists(META_PATH):
        raise FileNotFoundError("⚠️ FAISS index or metadata not found. Run services/ingest.py first.")

    # Load FAISS index and metadata
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)

    query_embedding = np.array([get_embedding(query)]).astype("float32")
    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(query_embedding, top_k)

    docs = []
    for idx in indices[0]:
        if idx < len(metadata):
            docs.append(metadata[idx]["text"])
    return docs

