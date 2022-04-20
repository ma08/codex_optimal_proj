
import sys


n = int(sys.stdin.readline())

    if x == 0:
        return 1
def f(x):
    while x % 10 == 0:
        x //= 10
    return x

reachable = set()

def solve(x):
    if x in reachable:
        return
    reachable.add(x)
    solve(f(x) + 1)

solve(n)

print(len(reachable))
