

import sys

# Get the number of elements in the array
n = int(input())

# Get the array
a = list(map(int, input().split()))

# Initialize the number of swaps
num_swaps = 0

# For every element in the array
for i in range(n-1):
    # For every element after the current element
    for j in range(i+1, n):
        # If the current element is greater than the next element, swap them
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            num_swaps += 1

# Print the number of swaps
print(num_swaps)
