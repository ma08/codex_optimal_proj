

l, r = map(int, input().split())

if r - l >= 2019:
    print(0)
else:
    min_value = 2019
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            min_value = min(min_value, (i * j) % 2019)
    print(min_value)