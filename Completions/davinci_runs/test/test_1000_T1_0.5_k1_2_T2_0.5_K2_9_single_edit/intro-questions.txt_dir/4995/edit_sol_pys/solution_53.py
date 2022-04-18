

# Number of observations
N = int(input())

# List of tuples (minutes, seconds)
data = []

# Get data from user
for i in range(N):
    data.append(tuple(int(x) for x in input().split()))
