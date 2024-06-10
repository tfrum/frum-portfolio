import numpy as np
import hashlib

def generate_numbers_and_hash(seed, n):
    # Input validation
    if not isinstance(seed, int):
        raise ValueError("Seed must be an integer")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Generate numbers using vectorized operation
    np.random.seed(seed)
    numbers = np.random.rand(n)

    # Create a bytes object from the numbers
    numbers_bytes = numbers.tobytes()

    # Create a hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the bytes of the numbers
    hash_object.update(numbers_bytes)

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()

    return hash_hex

# Example usage:
print(generate_numbers_and_hash(123, 10))