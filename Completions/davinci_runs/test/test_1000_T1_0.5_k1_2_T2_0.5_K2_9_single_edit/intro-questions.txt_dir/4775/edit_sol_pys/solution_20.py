

def main():
    """ Main function """
    word1, word2 = input().split()

    for i in range(len(word2)):
        for j in range(len(word1)):
            if word2[i] == word1[j]:
                print(word1, end="")
                break
            else:
                print(".", end="")
        print()

main()
