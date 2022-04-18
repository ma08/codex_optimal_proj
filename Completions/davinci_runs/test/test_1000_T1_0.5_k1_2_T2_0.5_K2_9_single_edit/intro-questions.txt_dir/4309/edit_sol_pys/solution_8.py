



def func(x):
    if x == 0:
        return 0
    else:
        return x + func(x - 1)


def func2(x):
    if x == 0:
        return 0
    else:
        return x + func2(x - 1)


def func3(x):
    if x == 0:
        return 0
    else:
        return x + func3(x - 1)


def func4(x):
    if x == 0:
        return 0
    else:
        return x + func4(x - 1)

import sys

N = int(sys.stdin.readline())

for i in range(100, N + 1):
    if len(set(list(str(i)))) == 1:
        print(i)
        break
