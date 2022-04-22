

X, K, D = map(int, input().split())

X = abs(X)
K = K - X // D
X = X % D
ans = X
if K % 2 == 1:
    ans = min(ans, abs(X - D))
print(ans)
