
import sys

def main():
    nums = [int(x) for x in sys.stdin.readline().split()]
    nums.sort()
    print(nums[2] - nums[0])

main()
