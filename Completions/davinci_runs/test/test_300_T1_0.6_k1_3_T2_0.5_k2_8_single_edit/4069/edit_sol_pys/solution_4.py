X, K, D = map(int, input().split())


if X < 0:
    X = abs(X)
    K = K % 2

if (K * D) > X:
    print(abs(X - (K * D)))
else:
    K = K - (X // D)
    X = X % D
    if K % 2 == 0:
        print(abs(X))
    else:
        print(abs(X - D))
