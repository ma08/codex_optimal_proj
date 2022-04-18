

from collections import deque

def main():
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(input())
    nums = list(dict.fromkeys(nums)) # remove duplicates
    print(len(nums))
    print(*nums)

main()
