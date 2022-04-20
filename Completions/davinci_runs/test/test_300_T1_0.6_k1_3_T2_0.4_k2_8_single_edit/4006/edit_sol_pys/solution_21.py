
import sys

n = int(sys.stdin.readline())

def f(x):
    while x % 10 == 0 and x > 0:
        x //= 10
    return x + 1

reachable = set()

def solve(x):
    if x in reachable:
        return
    reachable.add(x)
    solve(f(x))

solve(n)

print(len(reachable))
