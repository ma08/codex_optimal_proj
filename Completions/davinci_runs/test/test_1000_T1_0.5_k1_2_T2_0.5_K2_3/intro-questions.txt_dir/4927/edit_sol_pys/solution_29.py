
# https://codeforces.com/problemset/problem/1335/A
n, p, q = map(int, input().split())

if p > q:
    p, q = q, p

if (q - p) % (2 * n) < n:
    print("paul")
else:
    print("opponent")
