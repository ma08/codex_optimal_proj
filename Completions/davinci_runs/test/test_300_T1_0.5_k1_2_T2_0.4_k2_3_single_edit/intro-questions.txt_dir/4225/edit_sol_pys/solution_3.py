# https://atcoder.jp/contests/abc085/tasks/abc085_b

# A, B, C, K = map(int, input().split())
A, B, C, K = 2, 1, 1, 3

if K <= A:
    print(K)
elif K <= A+B:
    print(A)
else:
    print(A - (K - A - B))
