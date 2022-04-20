

import sys

# read inputs
inputs = sys.stdin.readlines()
inputs = [input.rstrip().split() for input in inputs]

# calculate time in world A
for j in range(len(inputs)):
    t = float(inputs[j][0])
    x = float(inputs[j][1])
    print(t / x)
