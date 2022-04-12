
import sys

def main():
    # Read in the input
    n = int(sys.stdin.readline())
    words = []
    for i in range(n):
        words.append(sys.stdin.readline().strip())
    
    # Check the input to see if the game was played correctly
    game_played_correctly = True
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            game_played_correctly = False
            break
    
    # Output the result
    if game_played_correctly:
        print("Fair game")
    else:
        print("Player {} lost".format(i%2 + 1))

if __name__ == "__main__":
    main()
