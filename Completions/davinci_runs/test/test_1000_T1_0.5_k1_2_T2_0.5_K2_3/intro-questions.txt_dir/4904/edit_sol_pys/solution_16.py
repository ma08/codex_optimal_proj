

import sys

def main():
    game = sys.stdin.readline().strip()

    # Abhishek starts with 0 points
    abhishek = 0
    # Akshay starts with 0 points
    akshay = 0

    # Iterate through the game history
    for i in range(0, len(game), 2):
        # If Abhishek scored
        if game[i] == 'A':
            # Add the points to her score
            abhishek += int(game[i + 1])
            # Check to see if she won
            if abhishek >= 11 and abhishek - akshay >= 2:
                print('A')
                break
        # If Akshay scored
        else:
            # Add the points to her score
            akshay += int(game[i + 1])
            # Check to see if she won
            if akshay >= 11 and akshay - abhishek >= 2:
                print('B')
                break


if __name__ == '__main__':
    main()
