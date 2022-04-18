N = int(input())
A = list(map(int, input().split()))


B = [0] * N

B[0] = A[0] - A[1] + 1
if B[0] < 0:
    B[0] = 0

A[0] = B[0] - B[1] + 1
if A[0] < 0:
    A[0] = 0

A[N-1] = B[N-2] - B[N-3] + 1
if A[N-1] < 0:
    A[N-1] = 0

for i in range(1, N-1):
    A[i] = (B[i-1] - B[i]) + (B[i] - B[i+1]) + 1
    if A[i] < 0:
        A[i] = 0

print(sum(A))
