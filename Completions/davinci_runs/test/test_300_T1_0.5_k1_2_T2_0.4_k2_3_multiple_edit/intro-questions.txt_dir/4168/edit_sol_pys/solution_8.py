
def get_bit(n, i):
    return (n >> i) & 1

def set_bit(n, i):
    return n | (1 << i)

def clear_bit(n, i):
    return n & ~(1 << i)

def toggle_bit(n, i):
    return n ^ (1 << i)

def get_bits_range(n, i, j):
    return (n >> i) & ~(~0 << (j - i + 1))

def set_bits_range(n, i, j, m):
    return n & ~(~(~0 << (j - i + 1)) << i) | (m << i)

def clear_bits_range(n, i, j):
    return n & ~(~(~0 << (j - i + 1)) << i)

def clear_bits_i_to_0(n, i):
    return n & ~(~0 << (i + 1))

def clear_bits_msb_to_i(n, i):
    return n & (~0 << (i + 1))

def update_bit(n, i, b):
    return n & ~(1 << i) | (b << i)
