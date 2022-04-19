def gcd_f(x, y):
    while y:
        x, y = y, x % y
    return x

n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd_f(gcd, t[i])

print(gcd)
