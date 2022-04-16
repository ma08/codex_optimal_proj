
import os
import sys

def main():
    word = sys.stdin.readline().strip()
    new_word = ""
    for i in range(0, len(word)):
        if word[i] in "aeiouAEIOU":
            new_word += word[i] + "p" + word[i]
        else:
            new_word += word[i]
    print(new_word)

if __name__ == "__main__":
    os.system("python3 file.py < file.txt")
