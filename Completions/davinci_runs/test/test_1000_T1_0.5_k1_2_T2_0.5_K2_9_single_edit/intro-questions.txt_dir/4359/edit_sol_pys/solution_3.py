

from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())
c = int(stdin.readline())
d = int(stdin.readline())
e = int(stdin.readline())

last = 0
last = max(last, a)
last = max(last, b)
last = max(last, c)
last = max(last, d)
last = max(last, e)

print(last)
