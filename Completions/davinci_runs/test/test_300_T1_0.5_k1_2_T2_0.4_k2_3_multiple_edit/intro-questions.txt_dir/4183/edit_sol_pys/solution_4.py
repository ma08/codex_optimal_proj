def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd(gcd, t[i])

print(gcd)
