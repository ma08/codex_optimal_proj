
# import sys
# Read input
N = int(input())

# Calculate the number of 1000-yen bills required
num_1000_yen_bills = int(N / 1000)

# Calculate the change
change = int(N % 1000)

# Print the change
print(change)
