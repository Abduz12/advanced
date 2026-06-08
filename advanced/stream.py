import random

class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

def xor_stream_cipher(text, seed):
    prng = LCG(seed)
    result = []
    for char in text:
        # Generate a pseudo-random byte (0-255) to XOR with the character
        keystream_byte = prng.next() % 256 
        encrypted_char = chr(ord(char) ^ keystream_byte)
        result.append(encrypted_char)
    return "".join(result)

# Testing LCG and XOR Cipher
message = "CONFIDENTIAL DATA"
seed = 12345

print("--- Generating PRNG Sequence ---")
gen = LCG(seed)
for _ in range(5):
    print(gen.next())

encrypted = xor_stream_cipher(message, seed)
decrypted = xor_stream_cipher(encrypted, seed)

print(f"\nOriginal: {message}")
print(f"XOR Encrypted (Raw): {repr(encrypted)}")
print(f"XOR Decrypted: {decrypted}")