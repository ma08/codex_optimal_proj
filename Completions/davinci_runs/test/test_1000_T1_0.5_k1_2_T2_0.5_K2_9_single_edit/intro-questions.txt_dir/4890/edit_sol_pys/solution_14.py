
import sys
import random

def solve(n, m, s, d):
    # Write your code here.
    # Return a list of length s with your solution.
    return [0] * s # Replace with your solution.

lines = sys.stdin.readlines()
n, m, s, d = [int(x) for x in lines[0].split()]
c = [int(x) for x in lines[2].split()]

res = solve(n, m, s, d)
if res == None:
    print("impossible")
else:
    print(" ".join([str(x) for x in res]))
