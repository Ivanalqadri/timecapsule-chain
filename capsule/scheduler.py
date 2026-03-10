from datetime import datetime
from capsule.storage import load_capsules
from capsule.decryptor import decrypt_message

def check_unlocks():

    capsules = load_capsules()

    for cap in capsules:

        unlock_date = datetime.fromisoformat(cap["unlock_date"])

        if datetime.utcnow() >= unlock_date:

            msg = decrypt_message(
                cap["key"],
                cap["nonce"],
                cap["ciphertext"]
            )

            print("\nUnlocked Capsule")
            print("-----------------")
            print(msg.decode())
