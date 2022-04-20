
import string
import sys

def main():
    n = int(input())
    s = input()
    for i in s:
        if i in string.ascii_uppercase:
            print(chr((ord(i) - ord('A') + n) % 26 + ord('A')), end="")
        elif i in string.ascii_lowercase:
            print(chr((ord(i) - ord('a') + n) % 26 + ord('a')), end="")
        else:
            print(i, end="")
    print()

if __name__ == "__main__":
    main()
