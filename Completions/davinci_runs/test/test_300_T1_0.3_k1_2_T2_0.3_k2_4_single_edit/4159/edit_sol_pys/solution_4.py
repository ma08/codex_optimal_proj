
a, b, k = map(int, input().split())

if a > k:
    a -= k
    k = 0
else:
    k -= a
    a = 0

if b > k:
    b -= k
    k = 0
else:
    k -= b
    b = 0

print(a, b)
