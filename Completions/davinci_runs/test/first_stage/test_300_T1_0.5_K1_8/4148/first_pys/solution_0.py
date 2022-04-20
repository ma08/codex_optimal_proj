

import sys


def main():
    num = int(sys.stdin.readline())
    string = sys.stdin.readline()
    for letter in string:
        print(chr(ord(letter) + num), end='')


if __name__ == '__main__':
    main()