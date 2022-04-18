

from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n, x, y = [int(x) for x in stdin.readline().strip().split()]
    print(x, y, end=' ')
    for i in range(n-2):
        x, y = y, x+y
        print(y, end=' ')
    print('')
