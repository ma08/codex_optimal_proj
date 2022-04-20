
import sys

def main():
    n = int(input())
    s = input()
    for c in s:
        if c != "Z":
            print(chr(ord(c) + n), end="")
        else:
            print(chr(ord(c) + n - 26), end="")

if __name__ == "__main__":
    main()
