

import sys

def main():
    game = sys.stdin.readline().strip()

    # Alice starts with 0 points
    alice = 0
    # Bob starts with 0 points
    bob = 0

    # Iterate through the game history
    for i in range(0, len(game), 2):
        # If Alice scored
        if game[i] == 'A':
            # Add the points to her score
            alice += int(game[i + 1])
            # Check to see if she won
            if alice >= 11 and alice - bob >= 2:
                print('Alice')
                break
        # If Bob scored
        else:
            # Add the points to her score
            bob += int(game[i + 1])
            # Check to see if she won
            if bob >= 11 and bob - alice >= 2:
                print('B')
                break


if __name__ == '__main__':
    main()
