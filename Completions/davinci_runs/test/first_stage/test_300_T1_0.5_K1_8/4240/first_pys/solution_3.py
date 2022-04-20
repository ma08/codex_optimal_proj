

import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if s == t:
    print("Yes")
    sys.exit()

for i in range(len(s)):
    s = s[1:] + s[0]
    if s == t:
        print("Yes")
        sys.exit()

print("No")