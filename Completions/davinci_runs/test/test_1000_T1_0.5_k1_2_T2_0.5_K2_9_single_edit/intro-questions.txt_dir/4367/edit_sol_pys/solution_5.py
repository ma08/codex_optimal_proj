
n, r = map(int, input().split())

print(r + 100 * (10 - n) if n < 10 else r)
