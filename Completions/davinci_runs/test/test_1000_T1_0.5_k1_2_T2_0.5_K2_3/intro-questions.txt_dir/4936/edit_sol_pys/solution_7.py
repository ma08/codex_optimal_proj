# This file contains the solution to the problem
# "The Maximum Subarray" in the file "Maximum Subarray.txt"

import sys

def main():
    n_cases = int(sys.stdin.readline())
    for _ in range(n_cases):
        n = int(sys.stdin.readline())
        arr = [int(x) for x in sys.stdin.readline().split()]
        max_sum = max_subarray_sum(arr)
        max_seq = max_subsequence_sum(arr)
        print(max_sum, max_seq)

def max_subarray_sum(arr):
    max_sum = 0
    max_ending_here = 0
    for x in arr:
        max_ending_here = max(max_ending_here + x, 0)
        max_sum = max(max_sum, max_ending_here)
    return max_sum

def max_subsequence_sum(arr):
    max_sum = 0
    for x in arr:
        if x > 0:
            max_sum += x
    if max_sum == 0:
        max_sum = max(arr)
    return max_sum

if __name__ == "__main__":
    main()
