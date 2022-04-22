

a, b, k = map(int, input().split())
# a, b, k = 2, 3, 3

if a > k:
    a -= k
else:
    k -= a
    a = 0
    if b > k:
        b -= k
    else:
        b = 0

print(a, b)
