

a,b,c,d = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return x * y // gcd(x, y)

def f(x, y):
    return x // y - (x - 1) // y

print(b - a + 1 - f(b, c) - f(b, d) + f(a - 1, c) + f(a - 1, d) - f(lcm(c, d), lcm(c, d))) 
