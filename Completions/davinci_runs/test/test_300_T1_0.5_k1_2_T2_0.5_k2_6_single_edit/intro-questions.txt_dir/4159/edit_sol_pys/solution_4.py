

a, b, c = map(int, input().split())
# a, b, c = 2, 3, 3
# a, b, c = 1000000000000, 1000000000000, 1000000000000

if a > c:
    a -= c
else:
    c -= a
    a = 0
    if b > c:
        b -= c
    else:
        b = 0

print(a, b, c)
