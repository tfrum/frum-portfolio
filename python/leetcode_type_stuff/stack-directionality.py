# In python we don't access to standard pointers, so we can't just dereference
# an object in memory to figure out whether the architecture we're on grows
# the stack up or down. We can get the ID, but it might not always indicate  it
# correctly. Of course... I don't have an ancient system that runs python to test
# grow-up stack morphology. iiwii

import ctypes
import sys

sys.setrecursionlimit(10000)


def check_stack_growth1():
    def get_id(obj):
        return id(obj) % 2**31

    before = get_id(1)
    after = get_id(2)

    if before < after:
        print("Stack grows up")
    elif before > after:
        print("Stack grows down")
    else:
        print("Unable to determine stack growth direction")


def check_stack_growth2():
    def recursive_call(n, ids):
        if n > 0:
            ids.append(id(n))
            recursive_call(n-1, ids)
    ids = []
    recursive_call(100, ids)
    growth = 'down' if ids[0] < ids[-1] else 'up'
    return f'{growth}.'



def check_stack_growth3():
    addresses = []

    def recursive_call(n):
        if n > 0:
            local_var = ctypes.c_void_p()
            addresses.append(ctypes.addressof(local_var))
            recursive_call(n - 1)

    recursive_call(10)
    growth = 'down' if addresses[0] > addresses[-1] else 'up'
    return f'The stack appears to grow {growth}.'

# The first three were trash AI answers these ones are mine playing around:

def get_address(y):
    x = y
    return ctypes.addressof(ctypes.c_int.from_address(id(x)))

def check_stack_growth():
    y = 1
    addr1 = get_address(y)
    y = 2
    addr2 = get_address(y)
    growth = 'down' if addr1 > addr2 else 'up'
    return f'{addr1}\n{addr2}\n{growth}.'


def get_addressc(obj):
    return ctypes.addressof(ctypes.py_object(obj))

def check_stack_growthc():
    y = 1
    addr1 = get_addressc(y)
    y = 2
    addr2 = get_addressc(y)
    growth = 'down' if addr1 > addr2 else 'up'
    return f'{addr1}\n{addr2}\n{growth}.'

print(check_stack_growthc())

# the best definitive answer that I could come up with
# fixes the issues of python reusing the same address space and
# thus returning the exact same ID between recursions
def check_stack_growth_recursive(depth, last_address=None):
    x = depth  # Local variable whose address we observe
    current_address = id(x)

    print(f"Depth: {depth}, Address of x: {current_address}")

    if depth <= 0:
        return

    if last_address is not None:
        growth = 'down' if current_address < last_address else 'up'
        print(f'{growth}.')


    check_stack_growth_recursive(depth - 1, current_address)


print(check_stack_growth1())
print(check_stack_growth2())
print(check_stack_growth3())
print(check_stack_growth())
check_stack_growth_recursive(50)