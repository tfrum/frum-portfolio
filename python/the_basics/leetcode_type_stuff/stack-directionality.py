# In python we don't access to standard pointers, so we can't dereference
# an object in memory to figure out whether the architecture we're on grows
# the stack up or down.
import ctypes

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
            ids.append(id(n))  # Record the memory address of the local variable `n`
            recursive_call(n-1, ids)
    ids = []
    recursive_call(100, ids)
    growth = 'down' if ids[0] < ids[-1] else 'up'  # Compare addresses
    return f'The stack appears to grow {growth}.'



def check_stack_growth3():
    addresses = []

    def recursive_call(n):
        if n > 0:
            local_var = ctypes.c_void_p()  # Create a local variable
            addresses.append(ctypes.addressof(local_var))  # Record its address
            recursive_call(n - 1)

    recursive_call(10)
    growth = 'down' if addresses[0] > addresses[-1] else 'up'
    return f'The stack appears to grow {growth}.'




print(check_stack_growth1())
print(check_stack_growth2())
print(check_stack_growth3())


def get_address():
    return id(ctypes.c_int())

def check_stack_growth():
    addr1 = get_address()
    addr2 = get_address()
    print(f'{addr1}\n{addr2}')
    growth = 'down' if addr1 > addr2 else 'up'
    return f'The stack appears to grow {growth}.'

print(check_stack_growth())