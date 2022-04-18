

from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n, a, b = [int(x) for x in stdin.readline().strip().split()]
    if n == 2: print(a, b)
    elif n == 3: print(a, b, a+b)
    elif n == 4: print(a, b, a+b, a*b)
    else:
        if n % 2 == 0: print(a, b, a+b, (n-4)//2*a*b, a*b, a+b, (n-4)//2*a*b, a*b)
        else:
            print(a, b, a+b, (n-5)//2*a*b, a*b, a+b, (n-5)//2*a*b, a*b, a)
