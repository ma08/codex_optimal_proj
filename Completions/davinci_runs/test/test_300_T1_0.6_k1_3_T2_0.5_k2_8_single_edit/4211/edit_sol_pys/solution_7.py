
N = int(input())
A = list(map(int, input().split()))

B = [0] * N

B[0] = A[0] - A[1] + 1
if B[0] < 0:
    B[0] = 0

B[N-1] = A[N-2] - A[N-3] + 1
if B[N-1] < 0:
    B[N-1] = 0

for i in range(1, N-1):
    B[i] = (A[i-1] - A[i]) + (A[i] - A[i+1]) + 1
    if B[i] < 0:
        B[i] = 0

print(sum(B))
