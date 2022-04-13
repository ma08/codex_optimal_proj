

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

g = gcd(gcd(a, b), c)

print(min(a//g, b//g, c//g)*7)
