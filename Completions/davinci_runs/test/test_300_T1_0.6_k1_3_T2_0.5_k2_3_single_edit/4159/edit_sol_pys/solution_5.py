
a, b, k = map(int, input().split())

for i in range(k):
    a, b = max(a - 1, 0), max(b - 1, 0)

print(a, b)
