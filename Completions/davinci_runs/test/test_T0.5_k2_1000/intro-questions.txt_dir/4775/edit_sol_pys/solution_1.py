

def main():
    """ Main function. """
    words = input().split()
    word1 = words[0]
    word2 = words[1]

    for i in range(len(word1)):
        if word1[i] in word2:
            print(word1[i], end="")
        else: print(".", end="")
    print()

main()
