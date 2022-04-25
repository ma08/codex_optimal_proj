import sys
input = sys.stdin.readline


N = int(input())

ans = 0 
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a * b <= N:
            ans += 1

print(ans) 
