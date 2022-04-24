
import sys, math

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    while len(nums) > 1:
        nums = nums[:-2] + [math.ceil((nums[-1] + nums[-2]) / 2)]
        nums.sort()
    print(nums[0])

if __name__ == '__main__':
    main()
