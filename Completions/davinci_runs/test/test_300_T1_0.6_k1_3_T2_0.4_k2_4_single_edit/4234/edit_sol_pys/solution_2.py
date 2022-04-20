

import sys

def good_string(s):
    for i in range(0, len(s)-1, 2):
        if s[i] == s[i+1]:
            return False
    return True

def delete_char(s):
    if good_string(s):
        return 0

    for i in range(len(s)):
        if good_string(s[:i] + s[i+1:]):
            return 1 + delete_char(s[:i] + s[i+1:])
    return 1 + delete_char(s[:-1])

def main():
    n = int(input())
    s = input()
    print(delete_char(s))

if __name__ == "__main__":
    main()
