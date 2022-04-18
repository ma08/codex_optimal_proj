
n, p, q = map(int, input().split())

if (q - p) % (2 * n) < n:
    print("opponent")
else:
    print("paul")
