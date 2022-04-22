

import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())

def solve(s):
    res = []
    last = 'a'
    for i in range(len(s)):
        if s[i] < last:
            res.append('1')
        else:
            res.append('0')
            last = s[i]
    return ''.join(res)

if s == sorted(s):
    print 'YES'
    print '0' * n
else:
    print 'YES'
    print solve(s)
