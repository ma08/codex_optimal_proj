
from collections import deque
from sys import stdin

s = stdin.readline().rstrip()
t = stdin.readline().rstrip()

def rotate(s):
    d = deque(s)
    d.rotate(-1)
    return ''.join(d)

print("No")
