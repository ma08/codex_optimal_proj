

import sys

def good_string(s):
    if len(s) % 2 == 0:  # if len(s) is even
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                return False
        return True
    else:  # if len(s) is odd
        return False

def delete_char(s):
    if len(s) == 1:  # base case
        return 0
    if good_string(s):  # if string is good, no more changes needed
        return 0

    for i in range(0, len(s), 2):  # if string is not good, find first pair of same chars
        if s[i] == s[i+1]:
            return 1 + delete_char(s[:i] + s[i+1:])  # delete the first pair of same chars and recurse

    if (len(s) % 2) == 1:  # if len(s) is odd
        return 1 + delete_char(s[:-1])  # delete the last char and recurse
    else:
        return 1 + delete_char(s[1:])  # delete the first char and recurse

def main():
    n = int(input())
    s = input()
    print(delete_char(s))
    print(s)

if __name__ == "__main__":
    main()
