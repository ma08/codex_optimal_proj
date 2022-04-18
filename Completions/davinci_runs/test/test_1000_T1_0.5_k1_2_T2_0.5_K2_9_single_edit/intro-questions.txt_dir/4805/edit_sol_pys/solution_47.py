

def main():
    # Read input
    phrase = raw_input()
    # Split input into words
    words = phrase.split()
    # Initialize a set of words
    unique_words = set()
    # Iterate over words
    for word in words: 
        # Check if word has already been added to set
        if word in unique_words:
            # If yes, print no and exit
            print("no")
            exit()
        # If not, add word to set
        else:
            unique_words.add(word)
    # If no word has been repeated, print yes
    print("yes")

if __name__ == "__main__":
    main()
