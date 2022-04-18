
from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline())
    nums = deque()
    for i in range(n):
        nums.append(int(stdin.readline()))
    nums = list(dict.fromkeys(nums))
    print(len(nums))
    print(*nums)

main()
