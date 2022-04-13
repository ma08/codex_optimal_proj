

def main():
    """ Main function."""
    words = input().split()
    word1 = words[0]
    word2 = words[1]

    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                print(word1)
                break
            else:
                print(".", end="")
        if word1[i] == word2[j]:
            break
        else:
            print()

main()
