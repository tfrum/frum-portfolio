import sys

def recursive_depth(depth, last_address=None):
    x = depth  # Local variable whose address we'll observe
    current_address = id(x)

    # Check and print the memory address of 'x'
    print(f"Depth: {depth}, Address of x: {current_address}")

    # Base case to stop the recursion after a depth is reached
    if depth <= 0:
        return

    # Compare addresses, if last_address is set
    if last_address is not None:
        if current_address > last_address:
            print("Stack appears to be growing upwards.")
        elif current_address < last_address:
            print("Stack appears to be growing downwards.")

    # Recursive call with depth decremented
    recursive_depth(depth - 1, current_address)

# Set a limit to the recursion depth to prevent a stack overflow
sys.setrecursionlimit(10000)

# Start the recursive function with an initial depth
try:
    recursive_depth(50)
except RecursionError:
    print("Reached maximum recursion depth!")
