

import sys

# Read the number of flowers
n = int(sys.stdin.readline())

# Read the heights of the flowers
h = [int(x) for x in sys.stdin.readline().split()]

# Initialize the count
count = 0;

# For each flower, if it is not at the right height, water it and all flowers to the left and right
for i in range(n): if h[i] != 0: count += 1; h = [h[j] + 1 if j < i else h[j] + 1 if j > i else h[j] for j in range(n)]

# Print the number of times the flowers were watered
print(count)
