
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()

for i in range(len(s)):
    if ord(s[i]) + n > ord("Z"):
        print(chr(ord(s[i]) + n - 26), end="")  # ord("Z") = 90
    else:
        print(chr(ord(s[i]) + n), end="")  # ord("Z") = 90
