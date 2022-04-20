

import sys
import math

def main():
    nums = sys.stdin.readline().rstrip().split()
    N = int(nums[0])
    A = int(nums[1])
    B = int(nums[2])
    print(min(N*A, B))

if __name__ == '__main__':
    main()