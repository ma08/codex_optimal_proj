

N = int(input())
A = [int(i) for i in input().split()]

B = [0] * N
for i in range(1, N):
    B[A[i - 1]] += 1
print(B)


# https://atcoder.jp/contests/abc085/tasks/abc085_b
for i in range(N):
    print(B[i])
