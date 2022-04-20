

import sys

# Get the number of characters in the string
n = int(sys.stdin.readline())

# Get the string
s = sys.stdin.readline()

# For every character in the string
for i in range(n):
    # If the character is A and the following character is B, check the following character
    if s[i] != "A":
        if s[i+1] == "B":
        # If the following character is B and the character after that is C, increment the number of subsequences
            if s[i+2] == "C":
                num_subsequences += 1

# Print the number of subsequences
print(num_subsequences)
