
from sys import stdin

def mod_max(x, y, n):
    return n - ((n - y) % x)

for _ in range(int(input())):
    x, y, n = map(int, input().split())
    print(mod_max(x,y,n))
