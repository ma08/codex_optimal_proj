
import math
import sys

def main():
    n = int(sys.stdin.readline())
    cans = [float(x) for x in sys.stdin.readline().split()]
    total = sum(cans)
    cans = [x/total for x in cans]
    cans = sorted(cans)
    cans = cans[::-1]
    print(cans)
    print(sum(cans[:n]))
    print(math.ceil(sum(cans[:n])))

if __name__ == '__main__':
    main()
