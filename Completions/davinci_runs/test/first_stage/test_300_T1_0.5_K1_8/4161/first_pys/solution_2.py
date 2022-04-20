

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

def lcm3(a, b, c):
    return lcm(lcm(a, b), c)

K = int(input())

ans = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            ans += gcd3(i, j, k)

print(ans)