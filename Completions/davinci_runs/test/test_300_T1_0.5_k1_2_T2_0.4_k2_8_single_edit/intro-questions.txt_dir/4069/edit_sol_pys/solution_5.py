
X, K, D = map(int, input().split())

if X < 0: X = -X

if X < K * D:
    K = K - (X - K * D) // (2 * D)
    X = (X - K * D) % (2 * D)

if X % (2 * D) == 0:
    print(X // (2 * D))
else:
    print(X // (2 * D) + 1)
