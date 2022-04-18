def gcd_f(x, y):
    if x < y:
        return gcd_f(y, x)
    if y == 0:
        return x
    return gcd_f(y, x % y)


n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd_f(gcd, t[i])

print(gcd)
