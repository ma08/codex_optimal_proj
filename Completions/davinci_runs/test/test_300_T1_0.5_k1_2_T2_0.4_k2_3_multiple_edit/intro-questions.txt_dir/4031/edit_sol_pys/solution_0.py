import sys
import os

sys.stdin = open(os.path.dirname(__file__) + '/in.txt', 'r')
sys.stdout = open(os.path.dirname(__file__) + '/out.txt', 'w')

n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

def find_max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

print(find_max_subarray(arr))
