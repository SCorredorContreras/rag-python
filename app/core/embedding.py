import os
from sentence_transformers import SentenceTransformer

MODEL_NAME = os.getenv("EMBEDDING_MODEL")
model = SentenceTransformer(MODEL_NAME)

def generar_embedding(texto: str) -> list[float]:
    return model.encode(texto).tolist()