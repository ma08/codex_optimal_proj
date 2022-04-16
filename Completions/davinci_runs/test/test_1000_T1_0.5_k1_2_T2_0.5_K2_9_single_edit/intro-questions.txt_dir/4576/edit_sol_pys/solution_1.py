

# get input
N = int(input())
K = int(input())
X = list(map(int, input().split()))

# initialize the minimum distance
min_dist = float('inf')

# loop over all combinations of the number of items
for i in range(N - K + 1):
    # calculate the distance
    dist = abs(X[i]) + abs(X[i + K - 1] - X[i])

# print the number of ways
print(num_ways)
