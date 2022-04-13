
# input
N = int(input())
A = list(map(int, input().split()))

# sort the list
A.sort()

# find the minimum distance
result = float('inf')
for i in range(1, N):
    result = min(result, A[i] - A[i-1])

# output
print(result)
