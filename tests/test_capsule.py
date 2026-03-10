from capsule.encryptor import encrypt_message
from capsule.decryptor import decrypt_message

def test_encrypt_decrypt():

    msg = b"hello future"

    enc = encrypt_message(msg)

    dec = decrypt_message(
        enc["key"],
        enc["nonce"],
        enc["ciphertext"]
    )

    assert dec == msg
