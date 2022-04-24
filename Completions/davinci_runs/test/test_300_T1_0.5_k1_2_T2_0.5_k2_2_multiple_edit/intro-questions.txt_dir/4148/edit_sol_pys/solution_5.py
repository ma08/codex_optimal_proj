

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

for i in range(len(s)):
    if s[i].islower():
        if ord(s[i]) + n > ord('z'):
            print(chr(ord(s[i]) + n - 26), end="")
        else:
            print(chr(ord(s[i]) + n), end="")
    elif s[i].isupper():
        if ord(s[i]) + n > ord('Z'):
            print(chr(ord(s[i]) + n - 26), end="")
        else:
            print(chr(ord(s[i]) + n), end="")
    else:
        print(s[i], end="")
