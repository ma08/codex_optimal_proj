import sys


h, n, m = map(int, sys.stdin.readline().split())

a = 0
b = 0

for i in range(1, h+1):
    a += (2*i - 1)
    b += (2*i)

if a <= n:
    print('0', m)
else:
    a -= n
    if a <= m*2:
        print(a//2, m - (a//2), sep=' ')
    else:
        print(m, '0', sep=' ')
