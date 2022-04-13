

import sys

n = int(sys.stdin.readline())

sournesses = []
bitternesss = []

for i in range(n):
    line = sys.stdin.readline().split()
    sournesses.append(int(line[0]))
    bitternesss.append(int(line[1]))

min_diff = 1000000000

for i in range(2**n):
    sournesses_sum = 1
    bitternesses_sum = 0
    for j in range(n):
        if (i >> j) % 2 == 1:
            sournesses_sum *= sournesses[j]
            bitternesses_sum += bitternesss[j]
    min_diff = min(min_diff, abs(sournesses_sum - bitternesses_sum))

print(min_diff)
