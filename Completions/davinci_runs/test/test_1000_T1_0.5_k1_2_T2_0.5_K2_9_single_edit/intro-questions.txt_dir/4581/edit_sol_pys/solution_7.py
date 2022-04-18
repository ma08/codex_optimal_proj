import sys


input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    s1 = set(list(S[:i]))
    s2 = set(list(S[i:]))
    ans = max(ans, len(s1 & s2))
print(ans)
