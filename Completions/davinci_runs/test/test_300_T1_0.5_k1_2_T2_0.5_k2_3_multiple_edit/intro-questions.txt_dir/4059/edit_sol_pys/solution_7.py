import sys
input = sys.stdin.readline


N = int(input())

ans = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        c = N - a * b
        if c > 0:
            ans += 1

print(ans)
