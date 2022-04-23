import sys
input = sys.stdin.readline


n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = 0
for i in range(n):
    if p[i] == q[i]:
        ans += 1

print(ans)
