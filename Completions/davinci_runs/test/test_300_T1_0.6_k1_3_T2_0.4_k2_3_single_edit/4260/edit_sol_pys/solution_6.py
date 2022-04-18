
import sys

# read inputs
inputs = sys.stdin.readlines()
inputs = [input.rstrip().split() for input in inputs]

# calculate time in world A
for i in range(len(inputs)):
    T = float(inputs[i][0])
    X = float(inputs[i][1])
    print(int(T / X))
