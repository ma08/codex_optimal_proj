

N = int(input())
B = list(map(int,input().split()))

A = [0] * N

A[0] = B[0] - max(0, B[1] - 1)
for i in range(1, N - 1):
    A[i] = B[i] - max(A[i - 1], B[i + 1])
A[N - 1] = B[N - 2]

print(sum(A))