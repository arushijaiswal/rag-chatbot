RAG Chatbot
RAG Chatbot is a Retrieval-Augmented Generation system that builds a FAISS vector
index from text documents.
It leverages LangChain and OpenAI embeddings to enable semantic search and
knowledge retrieval over your document corpus.

Features
- Load and process text documents with UTF-8 support
- Split large documents into manageable chunks for efficient embedding
- Generate embeddings using OpenAI’s text-embedding-3-small model
- Store embeddings in a FAISS vector database for fast retrieval
- Supports multilingual documents
  
Project Structure
rag-chatbot/
├── services/
│ └── ingest.py # Script to build FAISS index
├── data/ # Text documents 
├── faiss_index/ # Generated FAISS index 
├── venv/ # Python virtual environment 
└── README.md

Setup Instructions
1. Clone the repository
 git clone https://github.com/arushijaiswal/rag-chatbot.git
 cd rag-chatbot
2. Create and activate a Python virtual environment
 python -m venv venv
 # Windows
 venv\Scripts\activate
 # macOS/Linux
 source venv/bin/activate
3. Install dependencies
 pip install -r requirements.txt
4. Add your text documents
 Place .txt files in the data/ folder.
5. Build the FAISS index
 python -m services.ingest
 This will create a faiss_index/ folder with embedded vectors.
 
Notes
- Set your OpenAI API key in the environment variables before running embeddings.
- Large files such as the FAISS index and virtual environment are excluded via
.gitignore.
