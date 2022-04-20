
import sys

n = int(sys.stdin.readline())

reachable = set()

def solve(x):
    if x in reachable:
        return
    reachable.add(x)
    solve(x + 1)

solve(n)

print(len(reachable))
