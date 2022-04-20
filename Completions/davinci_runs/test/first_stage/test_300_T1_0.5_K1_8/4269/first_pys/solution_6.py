

import sys

S = sys.stdin.readline().rstrip()

if S[0] == S[1] or S[1] == S[2] or S[2] == S[3]:
    print("Bad")
else:
    print("Good")