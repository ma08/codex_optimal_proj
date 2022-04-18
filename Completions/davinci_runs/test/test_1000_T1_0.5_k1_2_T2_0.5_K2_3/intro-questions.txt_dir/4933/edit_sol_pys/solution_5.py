
import sys

def main():
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    diff = nums[1] - nums[0]
    print(nums[2] + diff)

if __name__ == '__main__':
    main()
