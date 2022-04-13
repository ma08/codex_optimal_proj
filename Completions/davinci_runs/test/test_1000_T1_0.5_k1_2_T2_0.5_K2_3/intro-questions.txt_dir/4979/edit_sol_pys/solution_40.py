
def get_bit(x, i):
    return (x >> i) & 1


print(get_bit(int(input()), 0))
