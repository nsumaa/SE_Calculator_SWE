def perform_and(a, b):
    return int(a) & int(b)

def perform_or(a, b):
    return int(a) | int(b)

def perform_xor(a, b):
    return int(a) ^ int(b)

def perform_not(a):
    return ~int(a)

def perform_left_shift(a, b):
    return int(a) << int(b)

def perform_right_shift(a, b):
    shift_count = int(b)
    if shift_count < 0:
        raise ValueError("Negative shift count")
    return int(a) >> shift_count