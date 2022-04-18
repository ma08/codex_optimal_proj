
# hello world
from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n, x, y = [int(x) for x in stdin.readline().strip().split()]
    if n == 2:
        print(x, y)
    elif n == 3:
        print(x, y, x+y)
    elif n == 4:
        print(x, y, x+y, x*y)
    else:
        if n % 2 == 0:
            print(x, y, x+y, (n-4)//2*x*y, x*y, x+y, (n-4)//2*x*y, x*y)
        else:
            print(x, y, x+y, (n-5)//2*x*y, x*y, x+y, (n-5)//2*x*y, x*y, x)
