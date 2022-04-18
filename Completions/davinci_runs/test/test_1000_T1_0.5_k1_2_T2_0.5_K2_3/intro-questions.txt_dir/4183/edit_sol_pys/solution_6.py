
def gcd_func(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_func(b, a % b)
