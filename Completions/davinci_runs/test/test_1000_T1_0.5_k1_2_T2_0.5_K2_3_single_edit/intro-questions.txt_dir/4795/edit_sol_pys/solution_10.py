

import math
import sys

def main():
    n = read_int_line()
    for _ in range(n):
        nums = read_int_line()
        print(solve(nums))

def solve(nums):
    return math.ceil(nums[0] / 2) * math.ceil(nums[1] / 2)

def read_int_line():
    return list(map(int, sys.stdin.readline().strip().split()))

if __name__ == '__main__':
    main()
