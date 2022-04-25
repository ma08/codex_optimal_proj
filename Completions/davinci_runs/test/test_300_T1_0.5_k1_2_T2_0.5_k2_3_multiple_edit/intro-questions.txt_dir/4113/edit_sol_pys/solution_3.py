
N, K = map(int, input().split())

X = list(map(int, input().split()))

ans = 0
for i in range(N-K+1):
    if X[i] < 0 and X[i+K-1] < 0:
        ans += X[i] * X[i+K-1]
    elif X[i] > 0 and X[i+K-1] > 0:
        ans += X[i] * X[i+K-1]
    else:
        ans += max(X[i], X[i+K-1])

print(ans)
