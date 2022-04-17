a, b, k = map(int, input().split())


if k <= a:  # kがa以下なら
    a -= k
else:
    k -= a
    a = 0
    if k <= b:  # kがb以下なら
        b -= k
    else:
        b = 0

print(a, b)
