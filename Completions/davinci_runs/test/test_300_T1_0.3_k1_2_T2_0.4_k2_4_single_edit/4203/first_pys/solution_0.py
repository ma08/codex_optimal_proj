

import sys

s = sys.stdin.readline().rstrip()

if s[0] == "A" and s[2:-1].count("C") == 1 and s[1:].islower():
    print("AC")
else:
    print("WA")