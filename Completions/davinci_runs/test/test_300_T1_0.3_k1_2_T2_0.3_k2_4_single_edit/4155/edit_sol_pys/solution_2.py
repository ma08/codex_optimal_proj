
import sys

# read input
n = int(sys.stdin.readline().rstrip())  # number of flowers
h = list(map(int, sys.stdin.readline().rstrip().split()))  # heights

# initialize
count = 0

# for each flower
for i in range(n):
    # if the flower is not at the right height
    if h[i] != 0:
        # water the flowers to the left
        for j in range(i):
            h[j] += 1
        # water the flowers to the right
        for j in range(i + 1, n):
            h[j] += 1
        # increment the count
        count += 1

# print the count
print(count)
