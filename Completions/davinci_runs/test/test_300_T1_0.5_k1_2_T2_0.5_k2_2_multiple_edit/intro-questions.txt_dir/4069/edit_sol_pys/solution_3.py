

X, K, D = map(int, input().split())
X = abs(X)

if X < 0:
    X = abs(X)

K = K - (X + K * D) // (2 * D)
X = (X + K * D) % (2 * D)

if X % (2 * D) == 0:
    print(X // (2 * D))
else:
    print(X // (2 * D) + 1)
