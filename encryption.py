from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=1000000)

def encrypt_file(input_file, output_file, password):
    salt = get_random_bytes(16)
    key = derive_key(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_GCM)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    with open(output_file, 'wb') as f:
        f.write(salt + cipher.nonce + tag + ciphertext)

def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    key = derive_key(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    with open(output_file, 'wb') as f:
        f.write(plaintext)