import sys

def main():
    line = sys.stdin.readline()
    while line:
        line = line.strip()
        words = line.split()
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
        line = sys.stdin.readline()

main()
