import numpy as np
import hashlib

def generate_numbers_and_hash(seed, n):
    # Input validation
    if not isinstance(seed, int):
        raise ValueError("Seed must be an integer")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    np.random.seed(seed)
    numbers = np.random.rand(n)

    numbers_bytes = numbers.tobytes()

    hash_object = hashlib.sha256()

    # Update the hash object with the bytes of the numbers
    hash_object.update(numbers_bytes)

    hash_hex = hash_object.hexdigest()

    return hash_hex

print(generate_numbers_and_hash(123, 10))