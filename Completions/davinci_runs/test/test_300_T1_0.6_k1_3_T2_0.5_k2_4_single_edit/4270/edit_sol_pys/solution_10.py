
import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(float, sys.stdin.readline().split()))
    nums.sort()
    while len(nums) > 1:
        nums = nums[:-2] + [float(nums[-1] + nums[-2]) / 2]
        nums.sort()
    print(nums[0])

if __name__ == '__main__':
    main()
