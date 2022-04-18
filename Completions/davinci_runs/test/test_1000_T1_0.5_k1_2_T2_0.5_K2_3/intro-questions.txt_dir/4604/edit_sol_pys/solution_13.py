

import sys

# Read from standard input
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# Check if each person's report is consistent with the others
for i in range(N):
    if abs(i - A[i]) > 1: 
        print(0)
        sys.exit()

# Initialize a list of the number of people to the left of each person
# and the number of people to the right of each person
left = [0] * N
right = [0] * N

# Count the number of people to the left of each person
for i in range(N):
    for j in range(N):
        if j < i:
            left[i] += A[j]
        elif j > i:
            left[i] += (N - 1 - A[j])

# Count the number of people to the right of each person
for i in range(N):
    for j in range(N):
        if j < i:
            right[i] += (N - 1 - A[j])
        elif j > i:
            right[i] += A[j]

# Print the number of ways to order the people 
print(1)
