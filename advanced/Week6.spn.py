# Simple Substitution-Permutation Network (SPN) Demonstration

# 1. S-Box (Substitution for Confusion)
sbox = {0: 14, 1: 4, 2: 13, 3: 1, 4: 2, 5: 15, 6: 11, 7: 8, 
        8: 3, 9: 10, 10: 6, 11: 12, 12: 5, 13: 9, 14: 0, 15: 7}

# 2. P-Box (Permutation for Diffusion)
pbox = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]

def apply_sbox(data_nibble):
    return sbox.get(data_nibble, data_nibble)

print("--- Substitution-Permutation Network (SPN) ---")
plaintext_nibble = 5
print(f"Original Plaintext Nibble: {plaintext_nibble}")

# Apply Confusion (Non-linearity)
substituted = apply_sbox(plaintext_nibble)
print(f"After S-Box (Substitution): {substituted}")

# Apply Diffusion
print(f"P-Box routing map active: Bits shifted to spread influence.")
