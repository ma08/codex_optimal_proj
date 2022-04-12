import sys

def next_reg(regs, i):
    if i == len(regs):
        return 0
    elif regs[i] == 20:
        regs[i] = 0
        return next_reg(regs, i+1)
    else:
        regs[i] += 1
        return 1

def main():
    regs = [1 for x in range(int(sys.stdin.readline()))]
    count = 0
    while next_reg(regs, 0) == 1:
        count += 1
    print(count)

if __name__ == '__main__':
    main()
