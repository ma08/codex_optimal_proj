
import sys

def main():
    word = sys.stdin.readline().strip()
    new_word = ""
    for i in range(len(word)):
        if word[i] in "aeiou":
            new_word += word[i] + "p" + word[i]
        else:
            new_word += word[i]
    print(new_word)

if __name__ == "__main__":
    main()
