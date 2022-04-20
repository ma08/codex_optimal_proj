
import sys

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[1])

if __name__ == '__main__':
    main()
