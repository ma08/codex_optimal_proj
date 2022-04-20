import sys

n = int(sys.stdin.readline())

def f(x):
    while x % 10 == 0 and x > 0:
        x //= 10
    return x + 1

reachable = set([n])

def solve(x):
    x = f(x)
    if x not in reachable:
        reachable.add(x)
        solve(x)

solve(n)

print(len(reachable))
