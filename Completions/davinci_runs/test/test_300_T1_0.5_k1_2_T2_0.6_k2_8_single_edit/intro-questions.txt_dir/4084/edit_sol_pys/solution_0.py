
n, a, b = map(int, input().split())
print(max(min(a, b), max(0, n - a - b)))
