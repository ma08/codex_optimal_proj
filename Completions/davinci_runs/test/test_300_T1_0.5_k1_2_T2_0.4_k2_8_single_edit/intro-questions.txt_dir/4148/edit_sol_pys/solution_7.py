
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

for i in range(len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        if ord(s[i]) + n > ord('Z'):
            print(chr(ord(s[i]) + n - 26), end="")
        else:
            print(chr(ord(s[i]) + n), end="")
    elif ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
        if ord(s[i]) + n > ord('z'):
            print(chr(ord(s[i]) + n - 26), end="")
        else:
            print(chr(ord(s[i]) + n), end="")
    else:
        print(chr(ord(s[i]) + n), end="")
