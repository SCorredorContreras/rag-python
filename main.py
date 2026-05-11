import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Colombia Comparte RAG")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routes.rag import router as rag_router
app.include_router(rag_router, prefix="/api")

if __name__ == "__main__":
    port = int(os.getenv("CHATBOT_PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)