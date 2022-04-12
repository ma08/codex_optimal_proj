

def main():
    """ Main function. """
    words = input().split()
    word1 = words[0]
    word2 = words[1]

    for i in range(len(word2)):
        for j in range(len(word1)):
            if word2[i] == word1[j]:
                print(word1)
                break
            else:
                print(".", end="")
        print()

main()
