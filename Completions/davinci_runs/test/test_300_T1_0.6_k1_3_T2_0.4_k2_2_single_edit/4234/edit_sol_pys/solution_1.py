#!/usr/bin/env python3

import sys

def good_string(s):
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            if s[i] == s[i + 1]:
                return False
        return True
    else:
        return False

def delete_char(s):
    if len(s) == 1:
        return 0
    if good_string(s):
        return 0

    for i in range(0, len(s), 2):
        if s[i] == s[i + 1]:
            return 1 + delete_char(s[:i] + s[i + 1:])

    if (len(s) % 2) == 1:
        return 1 + delete_char(s[:-1])
    else:
        return 1 + delete_char(s[1:])

def main():
    n = int(input())
    s = input()
    print(delete_char(s))
    print(s)

if __name__ == "__main__":
    main()
