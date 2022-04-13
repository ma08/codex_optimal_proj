

import sys
import os
import math

s, c, k = [int(x) for x in raw_input().split()]
d = [int(x) for x in raw_input().split()]

d.sort()

numMachines = 0

while len(d) > 0:
    numMachines += 1
    currentMachine = [d.pop(0)]
    for i in range(len(d)):
        if abs(d[i] - currentMachine[-1]) <= k:
            currentMachine.append(d.pop(i))
            i -= 1

    if len(currentMachine) > c:
        print("Too many socks for machine.")
        sys.exit(0)

print("Number of machines: " + str(numMachines))
