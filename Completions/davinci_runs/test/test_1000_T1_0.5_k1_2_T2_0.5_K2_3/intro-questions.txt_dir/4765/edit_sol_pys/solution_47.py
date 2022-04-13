

import sys

n = int(sys.stdin.readline())

sourness = []
bitterness = []

for i in range(n):
    line = sys.stdin.readline().split()
    sourness.append(int(line[0]))
    bitterness.append(int(line[1]))

min_diff = 1000000000

for i in range(2**n):
    sours = 1
    bitter = 0
    for j in range(n):
        if (i >> j) % 2 == 1:
            sours *= sourness[j]
            bitter += bitterness[j]
    min_diff = min(min_diff, abs(sours - bitter))

print(min_diff)
