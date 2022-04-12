

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

x, y, z = [int(x) for x in input().split()]

g = gcd(gcd(x, y), z)

print(min(x//g, y//g, z//g)*7)
