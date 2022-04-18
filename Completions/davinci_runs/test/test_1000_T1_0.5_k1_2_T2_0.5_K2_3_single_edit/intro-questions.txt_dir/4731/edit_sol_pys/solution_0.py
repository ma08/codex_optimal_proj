

from sys import stdin

def shiritori(words):
    """
    Returns "Fair Game" if the game was played according to the rules,
    otherwise returns "Player <i> lost"
    """
    words = [word.rstrip() for word in words[:-1]]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            return "Player {} lost".format(i%2+1)
    return "Fair Game"

def main():
    """
    Main function
    """
    num_words = int(stdin.readline())
    words = [stdin.readline().rstrip() for _ in range(num_words)]
    print(shiritori(words))

if __name__ == "__main__":
    main()
