
import sys

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    if n % 2 == 0:
        for i in range(0, n, 2):
            print(nums[i], end=' ')
        for i in range(n - 1, 0, -2):
            print(nums[i], end=' ')
    else:
        for i in range(0, n, 2):
            print(nums[i], end=' ')
        for i in range(n - 2, 0, -2):
            print(nums[i], end=' ')
        print(nums[-1], end=' ')

if __name__ == '__main__':
    main()
