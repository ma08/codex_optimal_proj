

N = int(input())
B = list(map(int, input().split()))

A = [0 for i in range(N)]
A[0] = B[0] // 2
A[-1] = B[-1] // 2

for i in range(1, N-1):
    A[i] = (B[i] - A[i-1]) // 2

print(sum(A))
