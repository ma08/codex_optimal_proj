

import sys
import math

n = int(sys.stdin.readline())

nums = list(input().split())

nums = sorted(nums, reverse=True)

print(nums[0])
