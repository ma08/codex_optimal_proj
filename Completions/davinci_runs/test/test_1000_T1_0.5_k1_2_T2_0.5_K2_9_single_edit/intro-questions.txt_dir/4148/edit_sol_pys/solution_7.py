
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

for i in range(len(s)):
    if ord(s[i]) + n > ord('Z'):
        sys.stdout.write(chr(ord(s[i]) + n - 26))
    else:
        sys.stdout.write(chr(ord(s[i]) + n))
