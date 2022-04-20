

import sys

# Read input and initialize
n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

# Initialize the count
count = 1

# For each element in b
for i in range(m):
    # If the element is not in a
    if b[i] not in a:
        # Print 0
        print(0)
        # Exit the program
        sys.exit()
    # If the element is not the first element in a
    if a.index(b[i]) != 0:
        # If the element is not the previous element in a
        if a.index(b[i]) != a.index(b[i - 1]) + 1:
            # Print 0
            print(0)
            # Exit the program
            sys.exit()
        # If the element is the previous element in a
        else:
            # Multiply the count by the distance between the element and the previous element
            count *= a.index(b[i]) - a.index(b[i - 1])

# Print the count modulo 1000000007
print(count)
