

# Solution

import sys

# Read the first line of input
line = sys.stdin.readline().strip()

# Initialize the state machine
state = 0

# Parse the input string
for c in line:
    # Check if the character is a valid move
    if c == 'R' or c == 'B':
        # If the character is a valid move, process it
        if c == 'R':
            # If the character is an R, check if the state is 0
            if state == 0:
                # If the state is 0, output an S and set the state to 1
                print('S', end='')
                state = 1
            else:
                # If the state is not 0, output an H and set the state to 0
                print('H', end='')
                state = 0
        elif c == 'B':
            # If the character is a B, check if the state is 0
            if state == 0:
                # If the state is 0, output a K and set the state to 1
                print('K', end='')
                state = 1
            else:
                # If the state is not 0, output an H and set the state to 0
                print('H', end='')
                state = 0
    else:
        if c == 'L':
            # If the character is an L, output an H and set the state to 0
            print('H', end='')
            state = 0
    else:
        # If the character is not a valid move, print an error and exit
        print('Invalid move: ' + c)
        exit(0)
