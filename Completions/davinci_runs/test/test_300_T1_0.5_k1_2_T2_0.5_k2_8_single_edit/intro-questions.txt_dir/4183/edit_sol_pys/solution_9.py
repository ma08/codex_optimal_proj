

def gcd_f(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_f(b, a % b)


print(gcd)
