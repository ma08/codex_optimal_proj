
from collections import deque

def main():
    n = int(input())
    nums = []
    for i in range(n):
        num = int(input())
        if num not in nums:
            nums.append(num)
    print(len(nums), *nums)


main()
