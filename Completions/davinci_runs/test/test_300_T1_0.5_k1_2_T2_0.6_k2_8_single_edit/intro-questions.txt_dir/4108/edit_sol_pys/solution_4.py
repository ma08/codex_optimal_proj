

import sys

def can_eq(s, t):
    if len(s) != len(t):
        return False
    for c in s:
        if c not in t:
            return False
        t = t.replace(c, '', 1)
    return True

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_eq(s, t):
    print('Yes')
else:
    print('No')
