#!/usr/bin/env python3

# Read input
N = int(input())

# Calculate the number of 500-yen bills required
num_500_yen_bills = N // 500  # 余りが出る

# Calculate the change
change = N % 500  # 余りが出る

# Print the change
print(change)
