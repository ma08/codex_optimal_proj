import sys

input = sys.stdin.readline

N = int(input())
S = input()

ans = 0
cnt = 0

for i in range(N):
    if S[i] == "I":
        cnt += 1
    else:
        cnt -= 1

    ans = max(ans, cnt)

print(ans)
