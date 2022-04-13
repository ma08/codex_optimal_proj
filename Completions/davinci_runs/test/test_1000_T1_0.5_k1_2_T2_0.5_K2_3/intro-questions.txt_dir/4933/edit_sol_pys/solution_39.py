import sys

def main(nums):
    nums = sorted(nums)
    diff = nums[2] - nums[0]
    return nums[2] + diff

if __name__ == '__main__':
    main()
