
import sys

def can_eq(s, t):
    if len(s) != len(t):
        return False
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    return s == t

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_eq(s, t):
    print('Yes')
else:
    print('No')
