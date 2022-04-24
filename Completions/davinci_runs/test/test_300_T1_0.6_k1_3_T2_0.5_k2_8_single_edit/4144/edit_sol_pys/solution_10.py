
N = int(input())

A = [0]*(N+1)
A[0] = 1
A[1] = 2
for i in range(2,N+1):
    A[i] = (2*A[i-1] - A[0])%(10**9+7)
print(A[N])
