

from sys import stdin

x, a, b = map(int, stdin.readline().split())
print(x - a if x - a > b else "safe")
