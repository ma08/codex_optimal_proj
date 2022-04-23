
def get_bit(n, i):
    return (n >> i) & 1

def set_bit(n, i, v):
    return (n & ~(1 << i)) | (v << i)
