import math
import sys

def main():
    """
    Main Function
    """
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    print(nums[0] + nums[1])

if __name__ == "__main__":
    main()
