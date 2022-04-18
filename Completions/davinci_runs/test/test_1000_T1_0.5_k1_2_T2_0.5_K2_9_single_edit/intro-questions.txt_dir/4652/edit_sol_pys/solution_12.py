
def solve(n, p):
    if n == 1: return True
    if n == 2: return p == [1, 2]
    if p[0] == 1:
        start = 1; direction = 1 if p[1] == 2 else -1
    else: start = p.index(1); direction = 1 if p[start - 1] == n else -1
    for i in range(n):
        if p[(start + direction * i) % n] != (i + 1) % n + 1: return False
    return True
for _ in range(int(input())):
    n = int(input()); p = list(map(int, input().split()))
    print("YES" if solve(n, p) else "NO")
