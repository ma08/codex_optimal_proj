

from sys import stdin

def shiritori_game(words):
    """
    Returns "Fair Game" if the game was played according to the rules,
    otherwise returns "Player <i> lost"
    """
    words = [word.rstrip() for word in words]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            return "Player {} lost".format(i%2+1)
    return "Fair Game"

def main():
    num_words = int(stdin.readline())
    words = [stdin.readline() for _ in range(num_words)]
    print(shiritori_game(words))

if __name__ == "__main__":
    main()
