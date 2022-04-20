

import sys

def main():
    n = int(sys.stdin.readline())
    words = sys.stdin.readline().split()

    # Build a dictionary of word frequencies
    word_map = {}
    for word in words:
        if word not in word_map:
            word_map[word] = 1
        else:
            word_map[word] += 1

    # Find the most frequently used word
    most_frequent = 0
    for word in word_map:
        if word_map[word] > most_frequent:
            most_frequent = word_map[word]

    # Find the length of the most frequently used word
    # and the number of words in the text
    length_of_most_frequent = 0
    for word in word_map:
        if word_map[word] == most_frequent:
            length_of_most_frequent = len(word)

    # The minimum length of the text after at most one abbreviation
    # is the length of the most frequently used word plus the number
    # of words in the text minus the most frequent word
    print(length_of_most_frequent + n - most_frequent)

main()