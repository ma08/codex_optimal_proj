

# A, B, C, K = map(int, input().split())
A, B, C, K = 2, 1, 1, 1

if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    print(A - (K - A - B))
