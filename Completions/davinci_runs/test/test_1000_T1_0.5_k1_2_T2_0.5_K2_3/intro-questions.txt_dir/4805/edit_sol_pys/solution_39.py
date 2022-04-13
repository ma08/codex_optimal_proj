

def main():
    # read input phrase
    phrase = input()
    # split phrase into words
    words = phrase.split()
    # initialize a set of unique words
    unique_words = set()
    # iterate over words
    for word in words:
        # check if word has already been added to set
        if word in unique_words:
            # if yes, print no and exit
            print("no")
            exit()
        # if not, add word to set
        else:
            unique_words.add(word)
    # if no word has been repeated, print yes
    print("yes")

if __name__ == "__main__":
    main()
