from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str
    session_id: str = ""
    top_k: int = 3