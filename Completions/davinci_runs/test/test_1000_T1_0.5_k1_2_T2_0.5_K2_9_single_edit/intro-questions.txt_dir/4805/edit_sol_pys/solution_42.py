

def main(): 
    # Read input
    words = input().split()
    # Create a set to store the words
    word_set = set()
    # Initialize a boolean flag
    no_repetition = True
    # Loop over the words
    for word in words:
        # Check if the word is already in the set
        if word in word_set:
            # If it is, change the flag to false and break the loop
            no_repetition = False
            break
        else:
            # If it isn't, add it to the set
            word_set.add(word)
    # Print the result
    print("yes" if no_repetition else "no")

if __name__ == "__main__":
    main()
