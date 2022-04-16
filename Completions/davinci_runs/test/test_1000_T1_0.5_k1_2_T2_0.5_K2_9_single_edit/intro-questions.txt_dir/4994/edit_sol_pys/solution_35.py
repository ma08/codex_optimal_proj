
import sys

def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    print(nums[0], nums[-1])

main()
