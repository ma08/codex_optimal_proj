

from collections import deque

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(input())
    nums = sorted(set(nums))
    for i in nums:
        print(i)

main()
