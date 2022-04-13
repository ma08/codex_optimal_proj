

from sys import stdin

def shiritori(words):
    """
    Returns "Fair Game" if the game was played according to the rules,
    otherwise returns "Player <i> lost"
    """
    words = [word.rstrip() for word in words]  # remove trailing newlines
    for i in range(1, len(words)):  # iterate through words
        if words[i][0] != words[i-1][-1]:  # if word does not start with last letter of previous word
            return "Player {} lost".format(i % 2 + 1)  # player i % 2 + 1 lost
    return "Fair Game"  # if game was played according to rules

def main():
    """
    Main function
    """
    num_words = int(stdin.readline())
    words = [stdin.readline() for _ in range(num_words)]
    print(shiritori(words))

if __name__ == "__main__":
    main()
