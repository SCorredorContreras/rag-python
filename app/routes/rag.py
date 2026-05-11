import json
import numpy as np
import faiss
from pathlib import Path
from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.core.embedding import generar_embedding
from app.core.llm import generar_respuesta


router = APIRouter()

BASE = Path(__file__).resolve().parents[2]
CHUNKS_PATH = BASE / "data/processed/chunks.jsonl"
INDEX_PATH = BASE / "indexes/faiss.index"

def _load():
    with CHUNKS_PATH.open("r", encoding="utf-8") as f:
        chunks = [json.loads(line) for line in f if line.strip()]
    index = faiss.read_index(str(INDEX_PATH))
    return chunks, index

try:
    chunks, index = _load()
except Exception:
    chunks, index = [], None

@router.post("/chat")
def chat(payload: ChatRequest):
    if index is None:
        return {"answer": "La base de conocimiento aún no está construida. Ejecuta build_knowledge_base.py primero."}
    vector = np.array([generar_embedding(payload.query)], dtype="float32")
    scores, indices = index.search(vector, payload.top_k)

    resultados = []
    for score, idx in zip(scores[0], indices[0]):
        if idx == -1 or float(score) < 0.25:
            continue
        resultados.append(chunks[int(idx)])

    if not resultados:
        return {"answer": "No tengo suficiente información para responder esa pregunta."}

    contexto = "\n\n".join(r["text"] for r in resultados)

    prompt = f"""Eres el chatbot oficial de Colombia Comparte. Responde en español natural y claro.
Usa únicamente la información del contexto. No inventes datos.

CONTEXTO:
{contexto}

PREGUNTA:
{payload.query}

RESPUESTA:"""

    return {"answer": generar_respuesta(prompt)}