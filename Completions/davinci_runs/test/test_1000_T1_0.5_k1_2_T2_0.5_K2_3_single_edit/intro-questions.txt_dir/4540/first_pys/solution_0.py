

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    print(abs(A[i] - A[i-1]) + abs(A[i] - A[(i+1)%N]) + abs(A[(i+1)%N] - A[i-1]))