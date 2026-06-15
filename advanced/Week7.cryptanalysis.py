# Cryptanalysis: Avalanche Effect Tester

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def calculate_avalanche(bin1, bin2):
    differences = sum(1 for a, b in zip(bin1, bin2) if a != b)
    total_bits = len(bin1)
    avalanche_percent = (differences / total_bits) * 100
    return differences, avalanche_percent

print("--- Cryptanalysis: Avalanche Effect Testing ---")
# Simulating a minor 1-character change in plaintext
cipher_output_1 = text_to_binary("CiphertextBlock_A")
cipher_output_2 = text_to_binary("CiphertextBlock_B") # One letter changed

diffs, percent = calculate_avalanche(cipher_output_1, cipher_output_2)

print(f"Bits altered in Ciphertext: {diffs}")
print(f"Avalanche Effect Ratio: {percent:.2f}%")
if percent >= 45:
    print("Conclusion: Cryptographically Strong (Resistant to linear attacks).")
else:
    print("Conclusion: Weak S-Boxes detected. Vulnerable to cryptanalysis.")
