import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

for i in range(len(s)):
    if ord(s[i]) + n > ord('Z') or (ord(s[i]) + n > ord('z') and ord(s[i]) <= ord('Z')):
        print(chr(ord(s[i]) + n - 26), end="")
    else:
        print(chr(ord(s[i]) + n), end="")
