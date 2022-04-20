

# input
N, K = map(int, input().split())
A = list(map(int, input().split()))[:N]

# sort
A.sort()

# compute
while len(A) > 1:
    if A[-1] - A[-2] > K:
        A = A[:-2] + [A[-1] - A[-2] - K]
    else:
        A = A[:-2]

# output
print(A[0])
