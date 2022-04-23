def gcd_func(a, b):
    if b == 0:
        return a
    else:
        return gcd_func(b, a % b)

n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd_func(gcd, t[i])

print(gcd)
