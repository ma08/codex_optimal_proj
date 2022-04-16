

import sys
import math

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    print(' '.join(map(str, nums)))
main()
