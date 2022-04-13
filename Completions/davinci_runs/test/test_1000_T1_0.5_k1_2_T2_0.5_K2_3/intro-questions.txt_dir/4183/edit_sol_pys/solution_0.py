def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
t = list(map(int, input().split()))

g = t[0]
for i in range(1, n):
    g = gcd(g, t[i])

print(g)
