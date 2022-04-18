

from sys import stdin

def mod_max(x, y, n): return n - ((n - y) % x)

for _ in range(int(stdin.readline().strip())): print(mod_max(*map(int, stdin.readline().strip().split())))
