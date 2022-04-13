

from collections import deque
import sys

def main():
    n = int(sys.stdin.readline())
    nums = deque()
    for i in range(n):
        nums.append(int(sys.stdin.readline()))
    nums = list(dict.fromkeys(nums))
    print(len(nums))
    print(*nums)

main()
