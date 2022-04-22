

import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
