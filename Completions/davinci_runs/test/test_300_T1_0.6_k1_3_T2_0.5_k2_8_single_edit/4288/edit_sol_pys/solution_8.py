
import sys

def main():
    nums = [int(x) for x in sys.stdin.readline().split()]
    nums.sort()
    print('Yes' if nums[0] == nums[1] or nums[1] == nums[2] else 'No')

main()
