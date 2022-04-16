
import sys

def main():
    line = sys.stdin.readline().strip()
    while line:
        words = line.split()
        if len(words) > 0:
            for word in words:
                newWord = ""
                i = 0
                while i < len(word):
                    if word[i] in "aeiou":
                        newWord += word[i:i+3]
                        i += 3
                    else:
                        newWord += word[i]
                        i += 1
                print(newWord, end="")
                print(" ", end="")
            print()
        line = sys.stdin.readline().strip()

main()
