

import sys

def good_string(s):
    if len(s) % 2 == 1:
        return False
    else:
        for i in range(0, len(s)-1, 2):
            if s[i] == s[i+1]:
                return False
        return True

def delete_char(s):
    if len(s) == 1 or good_string(s):
        return 0, s

    for i in range(0, len(s)-1, 2):
        if s[i] == s[i+1]:
            return 1 + delete_char(s[:i] + s[i+2:])

    if (len(s) % 2) == 1:
        return 1 + delete_char(s[:-1])
    else:
        return 1 + delete_char(s[1:])

def delete_char_iterative(s):
    if len(s) == 1 or good_string(s):
        return 0, s

    for i in range(0, len(s)-1, 2):
        if s[i] == s[i+1]:
            return 1 + delete_char_iterative(s[:i] + s[i+2:])

    if (len(s) % 2) == 1:
        return 1 + delete_char(s[:-1])
    else:
        return 1 + delete_char(s[1:])

def main():
    n = int(input())
    s = input()
    print(delete_char_iterative(s))

if __name__ == "__main__":
    main()
