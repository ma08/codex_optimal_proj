import sys

def main():
    hangman = sys.stdin.readline().strip().lower()
    alphabet = sys.stdin.readline().strip().lower()
    guessed = set()
    mistakes = 0
    while mistakes < 10:
        guess = alphabet[0]
        alphabet = alphabet[1:]
        if guess not in guessed:
            guessed.add(guess)
            if guess in hangman:
                if all(letter in guessed for letter in hangman):
                    print("WIN")
                    return
            else:
                mistakes += 1
        if mistakes >= 10:
            print("LOSE")
            return
        if all(letter in guessed for letter in hangman):
                print("WIN")
                return

if __name__ == "__main__":
    main()
