from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt_message(message: bytes):

    key = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)

    encrypted = aesgcm.encrypt(nonce, message, None)

    return {
        "key": key.hex(),
        "nonce": nonce.hex(),
        "ciphertext": encrypted.hex()
    }
