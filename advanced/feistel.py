def xor_strings(s1, s2):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def feistel_round(left, right, subkey):
    # F-function: simple XOR with a subkey for demonstration
    f_result = xor_strings(right, subkey)
    new_right = xor_strings(left, f_result)
    new_left = right
    return new_left, new_right

def simulate_feistel(plaintext_block, rounds, keys):
    # Split block in half
    mid = len(plaintext_block) // 2
    left = plaintext_block[:mid]
    right = plaintext_block[mid:]
    
    print(f"Initial: Left='{left}', Right='{right}'")
    
    for i in range(rounds):
        left, right = feistel_round(left, right, keys[i])
        print(f"Round {i+1}: Left='{left}', Right='{right}'")
        
    # Final swap
    return right + left

print("--- Feistel Cipher Simulation ---")
# Using a 4-character block, split into 2-char halves
block1 = "DATA" 
keys = ["K1", "K2"] # 2 rounds

cipher1 = simulate_feistel(block1, 2, keys)
print(f"Ciphertext 1: {repr(cipher1)}\n")

print("--- Avalanche Effect Test ---")
# Change just one letter in the plaintext (DATA -> DACA)
block2 = "DACA" 
cipher2 = simulate_feistel(block2, 2, keys)
print(f"Ciphertext 2: {repr(cipher2)}")

print(f"\nCompare Cipher 1 ({repr(cipher1)}) with Cipher 2 ({repr(cipher2)})")
print("Notice how changing one letter drastically changed the output.")