A, B, C, K = map(int, input().split())
# A, B, C, K = 2, 1, 1, 3


if A >= K:
    print(K)  # 1
elif A + B >= K:
    print(A)  # 2
else:
    print(A - (K - A - B))
