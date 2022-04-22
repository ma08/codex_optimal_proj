

from collections import deque

def main():
    n = int(input())
    nums = []
    for i in range(n):
        temp = int(input())
        if temp not in nums:
            nums.append(temp)
    print(len(nums))
    print(*nums)

main()
