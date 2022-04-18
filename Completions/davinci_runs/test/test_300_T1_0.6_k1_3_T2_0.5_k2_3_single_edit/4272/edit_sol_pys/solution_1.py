

import sys

# Get the number of strings
n = int(input())

# Get the strings
s = [input() for _ in range(n)]

# Initialize the number of strings equal to AC
num_strings = 0

# For every string
for i in range(n):
    # If the string doesn't contain AC, skip it
    if "AC" not in s[i]:
        continue 
    # If the string contains AC, increment the number of strings
    num_strings += 1

# Print the number of strings
print(num_strings)
