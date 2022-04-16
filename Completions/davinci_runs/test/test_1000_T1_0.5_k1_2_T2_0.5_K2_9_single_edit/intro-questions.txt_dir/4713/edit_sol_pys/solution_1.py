
from sys import stdin

n = int(stdin.readline())
s = stdin.readline()

x = 0
max_x = 0

for i in range(n):
    if s[i] == 'I':
        x += 1
    else:
        x -= 1
    if x > max_x:
        max_x = x

print(max_x)
