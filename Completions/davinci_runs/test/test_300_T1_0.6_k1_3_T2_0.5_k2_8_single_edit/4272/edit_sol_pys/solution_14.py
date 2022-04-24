

import sys, os

def main():
    # Get the number of characters in the string
    n = int(sys.stdin.readline())

    # Get the string
    s = sys.stdin.readline()

    # Initialize the number of contiguous subsequences equal to ABC
    num_subsequences = 0

    # For every character in the string
    for i in range(n):
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

if __name__ == "__main__":
    main()
