from fastapi import FastAPI
from capsule.encryptor import encrypt_message
from capsule.storage import save_capsule
from datetime import datetime
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TimeCapsule Chain running"}

@app.post("/create_capsule")
def create_capsule(message: str, unlock_date: str):

    encrypted = encrypt_message(message.encode())

    capsule = {
        "unlock_date": datetime.fromisoformat(unlock_date).isoformat(),
        **encrypted
    }

    save_capsule(capsule)

    # upload ke shelby storage
    subprocess.run(["shelby", "upload", "vault/capsules.json"])

    return {"status": "capsule created"}
