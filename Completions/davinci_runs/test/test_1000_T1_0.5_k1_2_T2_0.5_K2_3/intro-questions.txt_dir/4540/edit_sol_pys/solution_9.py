

N = int(input())
A = list(map(int, input().split()))

for i in range(1, N-1):

    print(abs(A[i] - A[i-1]) + abs(A[i] - A[i+1]) + abs(A[i+1] - A[i-1]))
