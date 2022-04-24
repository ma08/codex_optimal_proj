

import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
arr = list(map(int, input().split()))

curr_min = min(arr)
curr_max = max(arr)

print(curr_max - curr_min - 2*min(curr_max - curr_min, min(arr.count(curr_min), arr.count(curr_max))))
