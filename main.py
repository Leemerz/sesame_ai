cd ~/sesame_ai/sesame_ai

cat > main.py << 'PY'
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"ok": True}

# Optional demo endpoint to prove it works
@app.get("/ping")
def ping():
    return {"pong": True}
PY
