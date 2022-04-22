def gcd_f(a, b):
    return a if b == 0 else gcd_f(b, a % b)

n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd_f(gcd, t[i])

print(gcd)
