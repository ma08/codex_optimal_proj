

# input
N = int(input())
A = list(map(int, input().split()))

# sort
A.sort()

# output
print(A[N//2] - A[N//2 - 1])
