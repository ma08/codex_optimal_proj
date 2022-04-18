

def main():
    """ Main function """
    word1 = input()
    word2 = input()

    for i in range(len(word2)):
        for j in range(len(word1)):
            if word2[i] == word1[j]:
                print(word1)
                break
            else:
                print(".", end="")
        if word2[i] == word1[j]:
            break
        else:
            print()

main()
