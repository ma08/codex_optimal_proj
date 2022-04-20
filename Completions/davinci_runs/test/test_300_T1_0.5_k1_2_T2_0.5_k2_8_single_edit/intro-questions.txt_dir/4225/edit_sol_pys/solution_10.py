

 N, A, B = map(int, input().split())
# N, A, B = 3, 2, 10


if N <= A:
    print(N)
else:
    print(A)


# A, B, C, K = 2, 1, 1, 3

if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    print(A - (K - A - B))
