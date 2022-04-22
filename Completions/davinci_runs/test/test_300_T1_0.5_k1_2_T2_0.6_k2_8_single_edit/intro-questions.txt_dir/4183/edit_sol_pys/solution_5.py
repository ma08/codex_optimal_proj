def gcd_f(a, b):
    if a == 0 or b == 0:
        return 0
    if a % b == 0:
        return b
    return gcd_f(b, a % b)



n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd_f(gcd, t[i])

print(gcd)
