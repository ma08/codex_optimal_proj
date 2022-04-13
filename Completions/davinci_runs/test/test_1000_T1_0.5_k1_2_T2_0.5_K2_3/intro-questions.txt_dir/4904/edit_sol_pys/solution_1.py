

import sys

def main():
    game = sys.stdin.readline().strip()

    # Player 1 starts with 0 points
    player1 = 0
    # Player 2 starts with 0 points
    player2 = 0

    # Iterate through the game history
    for i in range(0, len(game), 2):
        # If Player 1 scored
        if game[i] == 'Player 1':
            # Add the points to her score
            player1 += int(game[i + 1])
            # Check to see if she won
            if player1 >= 11 and player1 - player2 >= 2:
                print('Player 1')
                break
        # If Player 2 scored
        else:
            # Add the points to her score
            player2 += int(game[i + 1])
            # Check to see if she won
            if player2 >= 11 and player2 - player1 >= 2:
                print('Player 2')
                break


if __name__ == '__main__':
    main()
