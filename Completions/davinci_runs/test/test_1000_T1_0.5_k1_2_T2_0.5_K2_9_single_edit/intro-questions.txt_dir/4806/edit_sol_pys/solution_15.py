
# Solution

import sys

def main():
    # Read the first line of input
    line = sys.stdin.readline()
    
    # Initialize the state machine
    state = 0
    
    # Parse the input string
    for c in line:
        # Check if the character is a valid move
        if c == 'R' or c == 'B' or c == 'L':
            # If the character is a valid move, process it
            if c == 'R':
                # If the character is an R, check if the state is 0
                if state == 0:
                    # If the state is 0, output an S
                    print('S', end='')
                    # Set the state to 1
                    state = 1
                else:
                    # If the state is not 0, output an H
                    print('H', end='')
                    # Set the state to 0
                    state = 0
            elif c == 'B':
                # If the character is a B, check if the state is 0
                if state == 0:
                    # If the state is 0, output a K
                    print('K', end='')
                    # Set the state to 1
                    state = 1
                else:
                    # If the state is not 0, output an H
                    print('H', end='')
                    # Set the state to 0
                    state = 0
            else:
                # If the character is an L, output an H
                print('H', end='')
                # Set the state to 0
                state = 0
        else:
            # If the character is not a valid move, print an error and exit
            print('Invalid move: ' + c)
            exit(0)
            
if __name__ == '__main__':
    main()
