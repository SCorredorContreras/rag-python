import os
from sentence_transformers import SentenceTransformer

MODEL_NAME = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
model = SentenceTransformer(MODEL_NAME)

def generar_embedding(texto: str) -> list[float]:
    return model.encode(texto).tolist()