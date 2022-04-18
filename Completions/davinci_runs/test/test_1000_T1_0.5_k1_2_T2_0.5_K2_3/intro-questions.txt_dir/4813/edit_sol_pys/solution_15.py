

import sys
import random

def main():
    hangman = sys.stdin.readline().strip().lower() #strip() removes trailing whitespace characters
    alphabet = sys.stdin.readline().strip() #readline() reads one entire line from the file
    guessed = set()
    components = 0
    while components < 10:
        guess = alphabet[0].lower()
        alphabet = alphabet[1:]
        if guess not in guessed:
            guessed.add(guess)
            if guess not in hangman:
                components += 1
            elif all(letter in guessed for letter in hangman):
                print("WIN")
                return
    print("LOSE")

if __name__ == "__main__":
    main()
