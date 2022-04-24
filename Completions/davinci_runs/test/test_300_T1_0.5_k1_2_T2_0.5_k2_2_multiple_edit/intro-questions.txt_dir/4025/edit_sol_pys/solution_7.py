

def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

a, b, c = [int(x) for x in input().split()]

g = gcd(gcd(a, b), c)

print(min(a//g, b//g, c//g) * 7)
