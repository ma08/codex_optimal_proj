

#import sys

def shift(n, s):
    s = list(s)
    for i in range(len(s)):
        s[i] = chr(((ord(s[i]) - 65 + n) % 26) + 65)
    return "".join(s)

#n = int(sys.stdin.readline())
#s = sys.stdin.readline().rstrip()

n = 2
s = "ABCXYZ"

print(shift(n, s))