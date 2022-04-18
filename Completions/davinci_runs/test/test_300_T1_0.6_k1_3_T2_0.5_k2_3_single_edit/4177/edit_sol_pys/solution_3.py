
import sys

s = sys.stdin.readline().rstrip()

for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        s = s[:i] + "x" + s[i+1:]

print(s)
