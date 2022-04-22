

a, b, x = map(int, input().split())
max_num = 10 ** 9

if a + b > x or a * max_num + b * len(str(max_num)) < x:
    print(0)
    exit()

k = (x - b) // a
l = len(str(k))

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))
