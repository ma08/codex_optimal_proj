

# Solution

import sys

def f(x):
    if x % 10 == 0:
        return f(x // 10)
    else:
        return x % 10

n = int(sys.stdin.readline())

f_n = f(n)

if f_n == 1:
    print(19)
else:
    print(20)