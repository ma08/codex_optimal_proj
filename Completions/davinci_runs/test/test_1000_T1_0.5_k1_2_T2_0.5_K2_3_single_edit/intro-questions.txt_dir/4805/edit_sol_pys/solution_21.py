
def main():
    # Read input and split into words
    words = input().split()
    # Initialize a set of unique words
    unique_words = set(words)
    # If the number of unique words is equal to the number of words
    # then no words were repeated
    if len(words) == len(unique_words):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
