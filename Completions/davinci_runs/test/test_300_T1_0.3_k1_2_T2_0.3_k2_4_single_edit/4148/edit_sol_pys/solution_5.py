
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()  # .rstrip() removes the newline character

for i in range(len(s)):
    if ord(s[i]) + n > 90:
        print(chr(ord(s[i]) + n - 26), end="")  # end="" prevents the newline character
    else:
        print(chr(ord(s[i]) + n), end="")
