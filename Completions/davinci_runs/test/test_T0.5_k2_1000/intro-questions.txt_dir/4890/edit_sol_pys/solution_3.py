
import sys
import random

def solve(n, m, s, d, c):
    return None

lines = sys.stdin.readlines()
n, m, s, d = [int(x) for x in lines[0].split()]
c = [int(x) for x in lines[1].split()]

res = solve(n, m, s, d, c)
if res is None:
    print("impossible")
else:
    print(" ".join([str(x) for x in res]))
