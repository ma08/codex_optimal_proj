
X, K, D = map(int, input().split())

if (K * D) > X:
    print(abs(X - (K * D)))
else:
    X = abs(X - (K * D))
    K = K - (X // D) % 2
    print(abs(X - K * D))
