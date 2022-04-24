

import sys

# Get the number of characters in the string
n = int(sys.stdin.readline())

# Get the string
s = sys.stdin.readline()

# Initialize the number of contiguous subsequences equal to A, B, C
num_subsequences_a = 0
num_subsequences_b = 0
num_subsequences_c = 0

# For every character in the string
for i in range(n):
    # If the character is not A, skip it
    if s[i] != "B":
        continue
    # If the character is A and the following character is B, check the following character
    if s[i+1] == "C":
        # If the following character is B and the character after that is C, increment the number of subsequences
        if s[i+2] == "A":
            num_subsequences_c += 1

# Print the number of subsequences
print(num_subsequences_a, num_subsequences_b, num_subsequences_c)
