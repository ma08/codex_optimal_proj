
import sys

def main():
    nums = [int(x) for x in sys.stdin.readline().split()]
    if nums[0] == nums[1] and nums[1] != nums[2]:
        print('Yes')
    elif nums[0] == nums[2] and nums[2] != nums[1]:
        print('Yes')
    elif nums[1] == nums[2] and nums[2] != nums[0]:
        print('Yes')
    else:
        print('No')

main()
