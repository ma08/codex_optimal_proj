import sys


s = input().strip()
t = input().strip()

try:
    for i in range(len(s)):
        if s[i] != t[2*i]:
            print(s[i], end='')
except IndexError:
    print("Out of range")
    sys.exit(1)
