

def main():
    # Get the input from the user
    sentence = input()
    # Get the words in the sentence
    words = sentence.split()
    # Reverse the words in the sentence
    words.reverse()
    # Output the reversed sentence
    print(' '.join(words))

if __name__ == '__main__':
    main()
