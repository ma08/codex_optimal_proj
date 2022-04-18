
import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())


def solve(s):
    last = s[0]
    for i in range(len(s)):
        if s[i] < last:
            s[i] = '1'
        else:
            s[i] = '0'
            last = s[i]
    return ''.join(s)


if s == sorted(s):
    print('yes')
    print('0' * n)
else:
    print('yes')
    print(solve(s))
