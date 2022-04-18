#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()

    for i in range(len(s)):
        if ord(s[i]) + n > ord('Z'):
            print("{}".format(chr(ord(s[i]) + n - 26)), end="")
        else:
            print("{}".format(chr(ord(s[i]) + n)), end="")
