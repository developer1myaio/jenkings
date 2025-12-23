from fastapi import FastAPI
import os

app = FastAPI(title="Jenkins + GitHub + Docker + FastAPI")

@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI deployed by Jenkins!",
        "env": os.getenv("APP_ENV", "local"),
        "version": os.getenv("APP_VERSION", "dev"),
    }

@app.get("/health")
def health():
    return {"status": "ok"}
