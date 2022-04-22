
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

def solve(s):
    last = 'a'
    out = []
    for c in s:
        if c < last:
            out.append('1')
        else:
            out.append('0')
            last = c
    return ''.join(out)

if s == sorted(s):
    print 'YES'
    print '0' * n
else:
    print 'YES'
    print solve(s)
