

import sys
import math
from collections import deque

def get_input():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, x, a

def get_max_sum(n, k, x, a):
    if k * x > n:
        return -1

    # if k = 1, then we repost all pictures
    if k == 1:
        return sum(a)

    # if k = n, then we repost the most beautiful picture
    if k == n:
        return max(a)

    # reposting the most beautiful pictures
    a_max = [max(a[i:i+k]) for i in range(n-k+1)]

    # a_max_sum[i] is the sum of the first i most beautiful pictures
    a_max_sum = [0]
    for i in range(len(a_max)):
        a_max_sum.append(a_max_sum[i] + a_max[i])

    # we repost the first x most beautiful pictures
    return a_max_sum[x]

def main():
    n, k, x, a = get_input()
    print(get_max_sum(n, k, x, a))

if __name__ == "__main__":
    main()