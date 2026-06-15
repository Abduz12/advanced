def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def vigenere_cipher(text, keyword, encrypt=True):
    result = ""
    keyword_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            shift = shift if encrypt else -shift
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def brute_force_caesar(ciphertext):
    print("--- Brute Forcing Caesar Cipher ---")
    for shift in range(1, 26):
        print(f"Shift {shift}: {caesar_cipher(ciphertext, shift, encrypt=False)}")

# Testing the Ciphers
plaintext = "SECURITY"
caesar_enc = caesar_cipher(plaintext, 4)
vig_enc = vigenere_cipher(plaintext, "KEY")

print(f"Plaintext: {plaintext}")
print(f"Caesar (Shift 4) Encrypted: {caesar_enc}")
print(f"Caesar Decrypted: {caesar_cipher(caesar_enc, 4, encrypt=False)}")
print(f"Vigenere (Key 'KEY') Encrypted: {vig_enc}")
print(f"Vigenere Decrypted: {vigenere_cipher(vig_enc, 'KEY', encrypt=False)}")

brute_force_caesar(caesar_enc)
