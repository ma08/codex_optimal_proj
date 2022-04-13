
import sys

def main():
    word = sys.stdin.readline().strip()
    new_word = ""
    for letter in word:
        if letter in "aeiou":
            new_word += letter + "p" + letter
        else:
            new_word += letter
    print(new_word)

if __name__ == "__main__":
    main()
