

n, p, q = map(int, input().split())

if p > q:
    p, q = q, p

if (q - p) % (2 * n) < n: # this is the condition
    print("paul")
else:
    print("opponent")
