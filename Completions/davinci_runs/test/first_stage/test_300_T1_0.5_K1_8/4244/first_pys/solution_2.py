

import sys

def main():
    n = int(sys.stdin.readline().strip())
    x = [int(x) for x in sys.stdin.readline().strip().split()]
    x.sort()
    m = (x[-1] - x[0]) / 2
    if m.is_integer():
        print(int(sum([(x_i - x[0] - m)**2 for x_i in x])))
    else:
        print(int(min(sum([(x_i - x[0] - m)**2 for x_i in x]), sum([(x_i - x[0] - m - 1)**2 for x_i in x]))))

if __name__ == '__main__':
    main()