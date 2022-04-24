

# Input
N = int(input())
A = list(map(int, input().split()))

# Sort
A.sort()

# Compute
while len(A) > 1:
    A = A[:-2] + [A[-1] - A[-2]]

# Output
print(A[0])
