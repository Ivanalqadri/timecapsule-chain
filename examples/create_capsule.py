from capsule.encryptor import encrypt_message
from capsule.storage import save_capsule
from datetime import datetime

message = input("Enter your secret message: ")

unlock = input("Unlock date (YYYY-MM-DD): ")

encrypted = encrypt_message(message.encode())

capsule = {
    "unlock_date": datetime.fromisoformat(unlock).isoformat(),
    **encrypted
}

save_capsule(capsule)

print("Capsule stored successfully.")
