import os
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from tqdm import tqdm
from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents(data_dir="data"):
    """
    Load all text documents from a directory recursively using UTF-8 encoding.
    """
    loader = DirectoryLoader(
        data_dir,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}  # ensures Unicode files load correctly
    )
    return loader.load()

def build_faiss_index(chunk_size=1000, chunk_overlap=100):
    """
    Build a FAISS vector index from documents in 'data' folder.
    """
    print("📂 Loading documents...")
    docs = load_documents()
    print(f"✅ Loaded {len(docs)} documents")

    # Split documents into smaller chunks safely
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(docs)
    print(f"✂️ Split into {len(texts)} chunks (chunk size: {chunk_size}, overlap: {chunk_overlap})")

    # Setup embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        timeout=60
    )

    # Embed chunks safely
    text_embeddings = []
    for t in tqdm(texts, desc="🔎 Embedding chunks"):
        try:
            vector = embeddings.embed_query(t.page_content)
            text_embeddings.append((t.page_content, vector))
        except Exception as e:
            print(f"❌ Skipped chunk due to embedding error: {e}")
            continue

    if not text_embeddings:
        print("⚠️ No embeddings created. Exiting.")
        return

    # Save to FAISS index
    print("💾 Saving FAISS index...")
    vectorstore = FAISS.from_embeddings(text_embeddings, embeddings)
    vectorstore.save_local("faiss_index")
    print("✅ FAISS index saved to 'faiss_index/'")

if __name__ == "__main__":
    build_faiss_index()
# This script builds a FAISS index from text documents in the 'data' directory.
# It handles loading, splitting, embedding, and saving the index.