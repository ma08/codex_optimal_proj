

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = [int(x) for x in input().split()]
print(gcd(a, b))
