
import sys

# Get the number of lines
n = int(input())

# Initialize the number of ABCs
num_abc = 0

# For every line
for i in range(n):
    # Get the string
    s = input()

    # Initialize the number of contiguous subsequences equal to ABC
    num_subsequences = 0

    # For every character in the string
    for j in range(len(s)):
        # If the character is not A, skip it
        if s[j] != "A":
            continue
        # If the character is A and the following character is B, check the following character
        if s[j+1] == "B":
            # If the following character is B and the character after that is C, increment the number of subsequences
            if s[j+2] == "C":
                num_subsequences += 1

    # Print the number of subsequences
    print(num_subsequences)
