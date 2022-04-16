def gcd_f(x, y):
    if y == 0:
        return x
    else:
        return gcd_f(y, x % y)


n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd_f(gcd, t[i])

print(gcd)
