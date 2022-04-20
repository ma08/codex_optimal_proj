

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max_subarray_sum(a))

def max_subarray_sum(a):
    """
    Returns the maximum subarray sum of a.
    """
    max_sum = a[0]
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

if __name__ == '__main__':
    main()
