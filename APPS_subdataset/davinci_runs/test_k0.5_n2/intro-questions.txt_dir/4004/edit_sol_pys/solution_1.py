n = int(input())
a = list(map(int, input().split()))

max_value = max(a)
min_value = min(a)

if (max_value - min_value) % 2 == 0:
    print((max_value - min_value) // 2)
else:
    print((max_value - min_value) // 2 + 1)
