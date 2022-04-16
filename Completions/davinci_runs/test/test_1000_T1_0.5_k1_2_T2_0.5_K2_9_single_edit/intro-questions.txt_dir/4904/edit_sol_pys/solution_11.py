
import sys

def main():
    game = sys.stdin.readline().strip()

    # Alice starts with 0 points
    alice = 0
    # Barbara starts with 0 points
    barbara = 0

    # Iterate through the game history
    for i in range(0, len(game), 2):
        # If Alice scored
        if game[i] == 'A' :
            # Add the points to her score
            alice += int(game[i + 1])
            # Check to see if she won
            if alice >= 11 and alice - barbara >= 2 :
                print('A')
                break
        # If Barbara scored
        else:
            # Add the points to her score
            barbara += int(game[i + 1])
            # Check to see if she won
            if barbara >= 11 and barbara - alice >= 2 :
                print('B')
                break


if __name__ == '__main__':
    main()
