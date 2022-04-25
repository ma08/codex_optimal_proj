

A, B, K = map(int, input().split())
# A, B, K = 2, 1, 3

if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    print(A - (K - A - B))
