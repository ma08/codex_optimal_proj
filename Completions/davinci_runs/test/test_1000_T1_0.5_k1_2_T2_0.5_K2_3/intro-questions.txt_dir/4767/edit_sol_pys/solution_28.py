import sys
import numpy as np
import math

def next_reg(regs, i):
    if i == len(regs):
        return 0
    elif regs[i] == 18:
        regs[i] = 0
        return next_reg(regs, i+1)
    else:
        regs[i] += 1
        return regs
def get_val(regs):
    return sum(regs)

def get_reg(val):
    regs = [0] * int(math.log(val, 18)) + [1]
    while get_val(regs) != val:
        regs = next_reg(regs, 0)
    return regs


def main():
    vals = [int(x) for x in sys.stdin.readline().split(' ')]
    print(np.array([get_reg(x) for x in vals]))


if __name__ == '__main__':
    main()
