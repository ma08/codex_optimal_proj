

A, B, C, K = map(int, input().split())  # A, B, C, K = 2, 1, 1, 3
# A, B, C, K = 2, 1, 1, 4

if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    print(A - (K - A - B))
