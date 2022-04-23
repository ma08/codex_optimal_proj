def gcd_func(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x



n = int(input())
t = list(map(int, input().split()))

gcd = t[0]
for i in range(1, n):
    gcd = gcd_func(gcd, t[i])

print(gcd)
