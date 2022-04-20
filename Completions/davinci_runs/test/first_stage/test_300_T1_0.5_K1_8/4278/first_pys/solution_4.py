

import sys
import collections

n = int(sys.stdin.readline())

result = 0

for i in range(n):
    s = sys.stdin.readline().rstrip()
    if len(s) != 10:
        continue

    c = collections.Counter(s)
    if i == 0:
        first = c
        continue
    if first == c:
        result += 1

print(result)