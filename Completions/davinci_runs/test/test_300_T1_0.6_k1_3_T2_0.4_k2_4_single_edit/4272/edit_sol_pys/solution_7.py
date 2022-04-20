

import sys

# Get the number of elements in the array
n = int(input())

# Get the array
a = list(map(int, input().split()))

# Initialize the number of elements in the array
num_elements = 0

# For every element in the array
for i in range(n):
    # If the element is not 0, increment the number of elements
    if a[i] != 0:
        num_elements += 1

# Print the number of elements
print(num_elements)
