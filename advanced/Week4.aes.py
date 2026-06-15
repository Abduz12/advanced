from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
print(f"Generated AES Key: {key.decode()}")

plaintext = b"Highly confidential patient records."
ciphertext = cipher.encrypt(plaintext)
print(f"Encrypted: {ciphertext}")
print(f"Decrypted: {cipher.decrypt(ciphertext).decode()}")
