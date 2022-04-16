

N = int(input())
A = list(map(int, input().split()))
S = 0

for i in range(N):
    S += abs(A[i] - A[i-1]) + abs(A[i] - A[(i+1)%N]) + abs(A[(i+1)%N] - A[i-1])

print(S)
