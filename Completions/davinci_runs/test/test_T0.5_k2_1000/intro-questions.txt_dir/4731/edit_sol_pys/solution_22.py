
from sys import stdin

def shiritori(words, num_players=2):
    """
    Returns "Fair Game" if the game was played according to the rules,
    otherwise returns "Player <i> lost".
    num_players is the number of players in the game.
    """
    words = [word.rstrip() for word in words] # remove newline characters
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            return "Player {} lost".format(i%num_players+1) # use modulo to determine player number
    return "Fair Game"

def main():
    """
    Main function
    """
    num_words = int(stdin.readline()) # read the first line to determine number of words
    words = [stdin.readline() for _ in range(num_words)] # read the words
    print(shiritori(words))

if __name__ == "__main__":
    main()
