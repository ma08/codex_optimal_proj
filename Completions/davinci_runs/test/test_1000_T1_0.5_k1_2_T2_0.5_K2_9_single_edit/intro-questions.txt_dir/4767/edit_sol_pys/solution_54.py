
import sys

def next_reg(regs, i):
    if i == len(regs):
        return 0
    elif regs[i] == 19:
        regs[i] = 0
        return next_reg(regs, i+1)
    else:
        regs[i] += 1
        return regs

def main():
    regs = [int(x) for x in sys.stdin.readline().split()]
    count = 0
    while next_reg(regs, 0):
        count += 1
    print(count) 

if __name__ == '__main__':
    main()
