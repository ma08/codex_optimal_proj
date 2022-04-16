
from sys import stdin

x = float(stdin.readline())

print(int(x*1000*5280/4854 + .5))
