

import sys, random

def main():
    n = int(sys.stdin.readline())
    nums = [int(x) for x in sys.stdin.readline().split()]
    nums.sort()
    min_diff = nums[-1] - nums[0]
    for i in range(n - 1):
        diff = nums[i + 1] - nums[i]
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

if __name__ == "__main__":
    main()
