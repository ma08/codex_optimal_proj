

def main():
    """ Main function """
    words = input().split()
    word1 = words[0]
    word2 = words[1]

    for i in word1:
        if i in word2:
            print(i, end="")
        else: 
            print(".", end="")
    print()

main()
