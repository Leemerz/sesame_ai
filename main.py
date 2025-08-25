import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
API_KEY = os.getenv("API_KEY")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/secure-endpoint")
def secure_endpoint(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "Access granted"}
