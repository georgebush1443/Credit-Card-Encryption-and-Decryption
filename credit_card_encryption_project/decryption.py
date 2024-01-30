# decryption.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_credit_card(encrypted_card_number, decryption_key):
    cipher = Cipher(algorithms.AES(decryption_key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_card_number = decryptor.update(encrypted_card_number) + decryptor.finalize()
    return decrypted_card_number.decode()
