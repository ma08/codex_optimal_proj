

# a, b, k = map(int, input().split())
# a, b, k = 2, 3, 3
a, b, k = 1000000000000, 1000000000000, 1000000000000

if a > k:  # 左側がkより大きい場合
    a -= k
else:  # 右側がkより大きい場合
    k -= a
    a = 0
    if b > k:
        b -= k
    else:
        b = 0

print(a, b)
