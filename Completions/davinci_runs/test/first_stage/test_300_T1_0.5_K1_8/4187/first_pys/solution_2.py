

import sys

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().strip().split()]

max_rest = 0
current_rest = 0
for i in range(n):
    if a[i] == 1:
        current_rest += 1
    else:
        max_rest = max(max_rest, current_rest)
        current_rest = 0
max_rest = max(max_rest, current_rest)

print(max_rest)