

import sys

def main():
    game = sys.stdin.readline().strip()

    # Alice starts at 0
    alice = 0;
    # Barbara starts at 0
    barbara = 0;

    # Iterate through the game
    for i in range(0, len(game), 2):
        # If Alice scored
        if game[i] == 'A':
            # Add the points to Alice's score
            alice += int(game[i + 1]);
        # If Barbara scored
        else:
            # Add the points to Barbara's score
            barbara += int(game[i + 1]);
        # Check to see if Alice won
        if alice >= 11 and alice - barbara >= 2:
            print('A');
            break;
        # Check to see if Barbara won
        if barbara >= 11 and barbara - alice >= 2:
            print('B');
            break;


if __name__ == '__main__':
    main()
