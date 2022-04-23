

import sys
import math

def main():
    nums = sys.stdin.readline().rstrip().split(' ')
    N = int(nums[0])  # number of items
    A = int(nums[1])  # price of one item
    B = int(nums[2])  # price of one package
    print(min(N*A, B))  # print the smaller one

if __name__ == '__main__':
    main()
