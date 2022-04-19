

from collections import deque, OrderedDict

def main():
    n = int(input())
    nums = deque()
    for i in range(n):
        nums.append(int(input()))
    nums = list(OrderedDict.fromkeys(nums))
    print(len(nums))
    print(*nums)

main()
