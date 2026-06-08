def simple_lfsr(seed, taps, length):
    state = seed
    output = []
    
    for _ in range(length):
        output.append(state[-1]) # Output the last bit
        # Calculate new bit based on XOR of tap positions
        new_bit = str(sum([int(state[t]) for t in taps]) % 2)
        # Shift right and insert new bit at the beginning
        state = new_bit + state[:-1]
        
    return "".join(output)

# Initial state and tap positions (e.g., tap positions 0 and 2)
initial_state = "1011" 
taps = [0, 2] 

print("--- LFSR Sequence Generation ---")
# Generate a sequence longer than 2^4 to show repetition
sequence = simple_lfsr(initial_state, taps, 30)
print(f"Generated Sequence: {sequence}")

print("\n--- Period Analysis ---")
# Manually pointing out where the sequence repeats
print("Notice how the pattern repeats. If an attacker intercepts enough")
print("of this keystream, they can use the Berlekamp-Massey algorithm")
print("to reconstruct the shift register and predict all future bits.")