
import sys

# read inputs
inputs = sys.stdin.readlines()
inputs = [input.strip().split() for input in inputs]

# calculate time in world A
for input in inputs:
    T = float(input[0])
    X = float(input[1])
    print(T / X)
