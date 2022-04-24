

a, b, k = map(int, input().split())  # map(関数, イテラブル)
# a, b, k = 2, 3, 3
# a, b, k = 1000000000000, 1000000000000, 1000000000000

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
