

import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline().split()
line = [int(i) for i in line]

print(n, line)

if max(line) < sum(line) - max(line):
    print("Yes")
else:
    print("No")
