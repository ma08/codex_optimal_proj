

a, b, x = map(int, input().split()) # a: 単価, b: 桁数, x: 合計金額

if a + b > x:
    print(0)
    exit()

k = (x - b) // a
l = len(str(k))

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))
