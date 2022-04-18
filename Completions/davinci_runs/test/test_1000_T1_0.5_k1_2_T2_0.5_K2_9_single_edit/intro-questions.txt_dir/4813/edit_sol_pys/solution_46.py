

import sys

def main():
    hangman = sys.stdin.readline().strip().lower()
    alphabet = sys.stdin.readline().strip().lower()
    guessed = set()
    components = 0
    while components < 10:
        guess = alphabet[0]
        alphabet = alphabet[1:]
        if guess not in guessed:
            guessed.add(guess)
            if guess not in hangman:
                components += 1
            if all(letter in guessed for letter in hangman):
                print("WIN")
                return
    print("LOSE")

if __name__ == "__main__":
    main()
