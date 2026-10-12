"""Minimal text processing service."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI(title="TextMVP")

class TextRequest(BaseModel):
    text: str
    operation: str = "upper"

class TextResponse(BaseModel):
    result: str
    operation: str
    char_count: int

@app.post("/process", response_model=TextResponse)
def process_text(req: TextRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    if req.operation == "upper":
        result = req.text.upper()
    elif req.operation == "lower":
        result = req.text.lower()
    elif req.operation == "reverse":
        result = req.text[::-1]
    elif req.operation == "words":
        result = " ".join(req.text.split()[::-1])
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")
    
    return TextResponse(
        result=result,
        operation=req.operation,
        char_count=len(result)
    )

def demo():
    from fastapi.testclient import TestClient
    client = TestClient(app)
    resp = client.post("/process", json={"text": "Hello World", "operation": "upper"})
    print(f"Status: {resp.status_code}")
    print(f"Body: {resp.json()}")
    assert resp.status_code == 200
    assert resp.json()["result"] == "HELLO WORLD"
    print("Demo passed!")
