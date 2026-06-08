def generate_binary_sequence(length, seed):
    import random
    random.seed(seed)
    return [random.choice([0, 1]) for _ in range(length)]

def frequency_test(sequence):
    zeros = sequence.count(0)
    ones = sequence.count(1)
    print(f"--- Frequency Test ---")
    print(f"Total Bits: {len(sequence)}")
    print(f"Zeros: {zeros} ({(zeros/len(sequence))*100:.2f}%)")
    print(f"Ones:  {ones} ({(ones/len(sequence))*100:.2f}%)")
    if abs(zeros - ones) < (len(sequence) * 0.1): # 10% tolerance
        print("Result: Pass (Good balance)")
    else:
        print("Result: Fail (Poor balance)")

def runs_test(sequence):
    runs = 1
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            runs += 1
    print(f"--- Runs Test ---")
    print(f"Total Runs: {runs}")
    print(f"Expected Runs roughly: {len(sequence)/2}")

# Execute Tests
seq = generate_binary_sequence(1000, 42)
print(f"Generated Sequence (first 50 bits): {seq[:50]}...\n")
frequency_test(seq)
print()
runs_test(seq)