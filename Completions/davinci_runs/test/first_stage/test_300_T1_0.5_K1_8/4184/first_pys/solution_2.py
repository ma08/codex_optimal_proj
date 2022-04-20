

N = int(input())
W = list(map(int, input().split()))

ans = sum(W)
for i in range(1 << N):
    s = 0
    for j in range(N):
        if i & (1 << j):
            s += W[j]
    ans = min(ans, abs(sum(W) - s - s))

print(ans)