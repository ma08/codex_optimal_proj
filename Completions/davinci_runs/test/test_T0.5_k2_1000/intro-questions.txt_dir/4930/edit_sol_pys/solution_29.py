#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        word = line.strip()
        new_word = ""
        for i in range(len(word)):
            if word[i] in "aeiou":
                new_word += word[i] + "p" + word[i]
            else:
                new_word += word[i]
        print(new_word)

if __name__ == "__main__":
    main()
