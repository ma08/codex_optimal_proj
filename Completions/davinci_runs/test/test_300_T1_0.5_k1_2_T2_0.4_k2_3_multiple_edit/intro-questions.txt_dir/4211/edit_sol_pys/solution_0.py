
N = int(input())
B = list(map(int, input().split()))
A = [0]*N

A[0] = B[0]
A[N-1] = B[N-1]

for i in range(1, N-1):
    A[i] = B[i] - A[i - 1]

print(sum(A))
