

n, p, q = map(int, input().split())

if p > q:
    p, q = q, p

if (q - p) % (2 * n) < n and (q - p) % (2 * n) != 0:
    print("paul")
else:
    print("opponent")
