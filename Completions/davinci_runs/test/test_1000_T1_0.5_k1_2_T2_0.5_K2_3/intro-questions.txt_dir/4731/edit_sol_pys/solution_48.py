

from sys import stdin

def shiritori(words: list) -> str:
    """
    Returns "Fair Game" if the game was played according to the rules,
    otherwise returns "Player <i> lost".
    """
    words_used = set()
    words = [word.rstrip() for word in words]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words_used:
            return "Player {} lost".format(i%2+1)
    return "Fair Game"

def main() -> None:
    """
    """
    num_words = int(stdin.readline())
    words = [stdin.readline() for _ in range(num_words)]
    print(shiritori(words))

if __name__ == "__main__":
    main()
