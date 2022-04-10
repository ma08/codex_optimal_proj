

import sys
import math

def get_median(nums, length):
    if length % 2 == 0:
        return (nums[length//2] + nums[length//2 - 1]) // 2
    else:
        return nums[length//2]

def main():
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    ans = 0
    for i in range(n):
        start = i
        end = n
        while start <= end:
            mid = (start + end) // 2
            median = get_median(nums[i:mid + 1], mid - i + 1)
            if median == m:
                ans += 1
                break
            elif median > m:
                end = mid - 1
            else:
                start = mid + 1
    print(ans)

if __name__ == "__main__":
    main()