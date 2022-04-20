

N = int(input())
W = list(map(int, input().split()))

# 前半と後半の和の差の絶対値を全探索
ans = float('inf')
for t in range(1, N):
    ans = min(ans, abs(sum(W[:t]) - sum(W[t:])))

print(ans)