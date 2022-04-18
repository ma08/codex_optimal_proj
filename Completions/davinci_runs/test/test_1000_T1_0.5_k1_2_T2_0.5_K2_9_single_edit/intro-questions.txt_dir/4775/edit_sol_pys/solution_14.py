

def main():
    """ Main function """
    words = input().split()
    word1 = words[0].upper()
    word2 = words[1].upper()

    for i in range(len(word2)):
        for j in range(len(word1)):
            if word2[i].upper() == word1[j].upper():
                print(word1[j], end="")
                break
            else:
                print(".", end="")
        if word2[i].upper() == word1[j].upper():
            break
        else:
            print()

main()
