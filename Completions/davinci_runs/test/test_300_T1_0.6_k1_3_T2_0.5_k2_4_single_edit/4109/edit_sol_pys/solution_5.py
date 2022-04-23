
import sys

def input():
    return sys.stdin.readline().strip()

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999

N = int(input())
A = list(map(int, input().split()))

dp = [INF] * (N + 1)
dp[0] = 0
dp[1] = 0

for i in range(1,N):
    dp[i+1] = min(dp[i+1], dp[i] + abs(A[i] - A[i+1]))
    if i + 2 <= N:
        dp[i+2] = min(dp[i+2], dp[i] + abs(A[i] - A[i+2]))

print(dp[N])
