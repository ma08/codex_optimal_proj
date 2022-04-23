
from math import ceil

X, K, D = map(int, input().split())

if K * D > X:
    print(X - (K * D))
else:
    K = K - ceil(X / D)
    X = X % D  # X = X - (X // D) * D
    if K % 2 == 0:
        print(X)
    else:
        print(X - D)
