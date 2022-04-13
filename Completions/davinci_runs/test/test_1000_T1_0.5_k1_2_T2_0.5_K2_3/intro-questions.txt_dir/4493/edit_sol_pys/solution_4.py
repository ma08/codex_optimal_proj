

import math
import sys

def main():
    # get input and put in array
    nums = list(map(int,input().split()))
    # sort array
    nums.sort()
    # print max - min
    print(nums[len(nums)-1] - nums[0])

if __name__ == "__main__":
    main()
