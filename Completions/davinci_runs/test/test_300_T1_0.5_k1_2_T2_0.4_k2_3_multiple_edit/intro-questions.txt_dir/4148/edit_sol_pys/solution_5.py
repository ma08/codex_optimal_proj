import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

for i in range(len(s)):
    if ord(s[i]) + n > ord('Z'):
        print(chr(ord(s[i]) + n - 26), end="")
    else:
        print(chr(ord(s[i]) + n), end="")
