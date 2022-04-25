import sys

s = str(sys.stdin.readline().rstrip())
n = len(s)

if n == 3 and s == '555':
    print('YES')
else:
    print('NO')
