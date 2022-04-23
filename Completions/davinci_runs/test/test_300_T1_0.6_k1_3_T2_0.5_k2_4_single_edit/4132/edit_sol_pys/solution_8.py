
# input
N = int(input())
A = list(map(int, input().split()))

# compute
A.sort(reverse=True)

while len(A) > 1:
    A = A[:-2] + [A[-1] - A[-2]]

# output
print(A[0])
