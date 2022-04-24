

import sys

# Get the number of lines in the file
n = int(sys.stdin.readline()) 

# For each line in the file
for i in range(n):
    # Get the line
    s = sys.stdin.readline()

    # Initialize the number of contiguous subsequences equal to ABC
    num_subsequences = 0

    # For every character in the string
    for i in range(len(s)):
        # If the character is not A, skip it
        if s[i] != "A":
            continue
        # If the character is A and the following character is B, check the following character
        if s[i+1] == "B":
            # If the following character is B and the character after that is C, increment the number of subsequences
            if s[i+2] == "C":
                num_subsequences += 1

    # Print the number of subsequences
    print(num_subsequences)
