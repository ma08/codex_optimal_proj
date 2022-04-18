import math

import sys

def main():
    nums = [int(x) for x in sys.stdin.readline().strip().split()]
    n = nums[0]
    k = nums[1]
    if k == 0:
        print(n)
    else:
        print(math.ceil(n/k))

if __name__ == '__main__':
    main()
