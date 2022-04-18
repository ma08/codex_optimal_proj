

import sys
import re

def main():
    lines = [line.strip() for line in sys.stdin]
    word = lines[0]
    ending_lists = [line.split() for line in lines[2:2 + int(lines[1])]]
    phrases = lines[4 + int(lines[1]):]

    for phrase in phrases:
        words = phrase.split()
        if len(words) == 2:
            if word_ends_with(words[0], ending_lists) and word_ends_with(words[1], ending_lists):
                print("YES")
            else:
                print("NO")
        else:
            if word_ends_with(words[0], ending_lists) and word_ends_with(words[2], ending_lists):
                print("YES")
            else:
                print("NO")

def word_ends_with(word, ending_lists):
    for endings in ending_lists:
        if word[-len(endings[0]):] in endings:
            return True
    return False

if __name__ == "__main__":
    main()
