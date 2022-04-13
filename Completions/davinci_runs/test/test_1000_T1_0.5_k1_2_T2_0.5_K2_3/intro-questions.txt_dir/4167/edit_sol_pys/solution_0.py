#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    nums = []
    for i in range(n):
        nums.append(int(sys.stdin.readline()))
    nums.sort()
    ans = 0
    for i in range(1, n + 1):
        ans += abs(nums[i - 1] - i)
    print(ans)


if __name__ == '__main__':
    main()
