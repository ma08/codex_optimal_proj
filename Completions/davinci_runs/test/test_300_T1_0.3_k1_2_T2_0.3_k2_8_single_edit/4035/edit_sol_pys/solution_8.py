

import sys
a, b = map(int, sys.stdin.readline().split())

for i in range(1, 101):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        print(i)
        exit()

print(-1)
