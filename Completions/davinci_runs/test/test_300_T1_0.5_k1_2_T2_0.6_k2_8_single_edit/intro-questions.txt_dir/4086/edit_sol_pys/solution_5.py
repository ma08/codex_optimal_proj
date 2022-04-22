

from collections import deque

def main():
    n = input()
    nums = deque()
    for i in range(int(n)):
        nums.append(input())
    nums = list(dict.fromkeys(nums))
    print(len(nums))
    print(*nums)

main()
