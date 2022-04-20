

from sys import stdin

a, b = map(int, stdin.readline().split())
print(0 if a < b else 10)
