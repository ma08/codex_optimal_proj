
a, b = map(int, input().split())
print(a - a % 10 ** b + 10 ** b if a % 10 ** b >= 5 * 10 ** (b - 1) else a - a % 10 ** b)
