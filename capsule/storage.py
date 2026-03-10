import json
import os

VAULT_FILE = "vault/capsules.json"

def load_capsules():

    if not os.path.exists(VAULT_FILE):
        return []

    with open(VAULT_FILE, "r") as f:
        return json.load(f)

def save_capsule(capsule):

    capsules = load_capsules()
    capsules.append(capsule)

    with open(VAULT_FILE, "w") as f:
        json.dump(capsules, f, indent=2)
