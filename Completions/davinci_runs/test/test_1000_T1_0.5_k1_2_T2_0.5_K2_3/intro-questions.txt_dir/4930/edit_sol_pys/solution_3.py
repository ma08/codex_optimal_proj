
import sys

def main():
    line = sys.stdin.readlines()
    for l in line:
        l = l.strip()
        words = l.split()
        newWord = ""
        for word in words:
            for i in range(len(word)):
                if word[i] in "aeiouAEIOU":
                    newWord = newWord + word[i:i+3]
                    break
                else:
                    newWord = newWord + word[i]
        print(newWord)

main()
