
import sys

def main():
    game = sys.stdin.readline().strip().split(',')

    # A starts with 0 points
    A = 0
    # B starts with 0 points
    B = 0

    # Iterate through the game history
    for i in range(0, len(game)):
        # If A scored
        if game[i] == 'A':
            # Add the points to her score
            A += int(game[i][1])
            # Check to see if A won
            if A >= 11 and A - B >= 2:
                print('A')
                break
        # If B scored
        else:
            # Add the points to her score
            B += int(game[i][1])
            # Check to see if B won
            if B >= 11 and B - A >= 2:
                print('B')
                break


if __name__ == '__main__':
    main()
