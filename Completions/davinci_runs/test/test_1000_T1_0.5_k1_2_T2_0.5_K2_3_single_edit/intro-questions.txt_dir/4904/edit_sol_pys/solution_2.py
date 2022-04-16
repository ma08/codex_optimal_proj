
import sys

def main():
    game = sys.stdin.readline().strip() #type string

    # Alice starts with 0 points
    alice = 0   #type int
    # Barbara starts with 0 points
    barbara = 0   #type int

    # Iterate through the game history
    for i in range(0, len(game), 2): #type int
        # If Alice scored
        if game[i] == 'A':  #type string
            # Add the points to her score
            alice += int(game[i + 1]) #type int
            # Check to see if she won
            if alice >= 11 and alice - barbara >= 2: #type int
                print('A') #type string
                break #type string
        # If Barbara scored
        else:
            # Add the points to her score
            barbara += int(game[i + 1]) #type int
            # Check to see if she won
            if barbara >= 11 and barbara - alice >= 2:
                print('B')
                break


if __name__ == '__main__':
    main()
