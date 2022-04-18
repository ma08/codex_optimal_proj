
import sys
sys.setrecursionlimit(100000)

def get_input():
    inputs = []
    for i in range(4):
        inputs.append(list(map(int, input().split())))
    return inputs
