

def gcd(u, v):
    while v:
        u, v = v, u % v
    return u

u, v, w = [int(x) for x in input().split()]

g = gcd(gcd(u, v), w)

print(min(u//g, v//g, w//g)*7)
