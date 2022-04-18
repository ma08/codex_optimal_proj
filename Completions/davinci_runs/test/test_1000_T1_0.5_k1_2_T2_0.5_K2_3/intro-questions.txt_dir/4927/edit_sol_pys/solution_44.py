n, p, q = map(int, input().split())
p, q = min(p, q), max(p, q)

if (q - p) % (2 * n) < n or (q - p) % (2 * n) == n:
    print("paul")
else:
    print("opponent")
