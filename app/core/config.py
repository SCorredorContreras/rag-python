import os
from dotenv import load_dotenv

load_dotenv(override=True)

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "indexes/faiss.index")
TOP_K_RETRIEVAL = int(os.getenv("TOP_K_RETRIEVAL", "3"))