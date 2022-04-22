# gcd
def gcd_f(a, b):
    if a > b:
        a, b = b, a
    while a != 0:
        a, b = b % a, a
    return b


n = int(input())
a = list(map(int, input().split()))

gcd = a[0]
for i in range(1, n):
    gcd = gcd_f(gcd, a[i])

print(gcd)
