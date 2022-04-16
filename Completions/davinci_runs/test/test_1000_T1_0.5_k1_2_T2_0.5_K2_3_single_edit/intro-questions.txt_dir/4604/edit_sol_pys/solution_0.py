
import sys

# Read from standard input
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# Check if each person's report is consistent with the others
for i in range(N):
    if abs(i - A[i]) > 1:
        print(0)
        sys.exit()

# Initialize a list to keep track of the number of people we have ordered
num_ways = [0] * N
num_ordered = 0

# Order the people
while num_ordered < N:
    # Find the first person that has not been ordered
    i = A.index(0)

    # Add this person to the ordered list and remove them from the list of people to order
    num_ways[num_ordered] = i
    num_ordered += 1
    A = [x - 1 if x > i else x for x in A]

# Print the number of ways to order the people
print(num_ways[0])
