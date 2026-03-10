from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def decrypt_message(key, nonce, ciphertext):

    key = bytes.fromhex(key)
    nonce = bytes.fromhex(nonce)
    ciphertext = bytes.fromhex(ciphertext)

    aesgcm = AESGCM(key)

    return aesgcm.decrypt(nonce, ciphertext, None)
