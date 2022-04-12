

from sys import stdin

def shiritori(words, num_players=2):
    """
    Returns "Fair Game" if the game was played according to the rules,
    otherwise returns "Player <i> lost".
    num_players is the number of players in the game.
    """
    words = [word.strip() for word in words]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            return "Player {} lost".format(i%num_players+1)
    return "Fair Game"

def main():
    """
    Main function
    """
    num_words = int(stdin.readline())
    words = [stdin.readline() for _ in range(num_words)]
    print(shiritori(words))

if __name__ == "__main__":
    main()
