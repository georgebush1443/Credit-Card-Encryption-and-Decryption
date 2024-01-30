# encryption.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_credit_card(card_number, encryption_key):
    cipher = Cipher(algorithms.AES(encryption_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_card_number = encryptor.update(card_number.encode()) + encryptor.finalize()
    return encrypted_card_number
