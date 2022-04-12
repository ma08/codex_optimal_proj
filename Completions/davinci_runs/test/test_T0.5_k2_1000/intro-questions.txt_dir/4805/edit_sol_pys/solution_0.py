
def main():
    # read input
    words = input().split()
    # create a set to store the words
    word_set = set()
    # initialize a boolean flag
    no_repetition = True
    # loop over the words
    for word in words:
        # check if the word is already in the set
        if word in word_set:
            # if it is, change the flag to false and break the loop
            no_repetition = False
            break
        else:
            # if it isn't, add it to the set
            word_set.add(word)
    # print the result
    print("yes" if no_repetition else "no")


if __name__ == "__main__":
    main()
