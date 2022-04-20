
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

for i in s:
    if ord(i) + n > 90:
        print(chr(ord(i) + n - 26), end="")
    elif ord(i) + n < 65:
        print(chr(ord(i) + n + 26), end="")
    elif ord(i) + n <= 90:
        print(chr(ord(i) + n), end="")
