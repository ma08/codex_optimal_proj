
def gcd_f(a, b):
    if b == 0:
        return a
    else:
        return gcd_f(b, a % b)
