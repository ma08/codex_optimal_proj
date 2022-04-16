
from sys import stdin

N = int(stdin.readline())
S = stdin.readline()

x = 0
max_x = 0

for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    if x > max_x:
        max_x = x

print(max_x)
