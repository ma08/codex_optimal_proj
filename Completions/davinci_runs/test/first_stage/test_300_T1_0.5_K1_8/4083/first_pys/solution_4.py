

from math import log2

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

# if the largest number is already a multiple of 2^k, we don't need to do anything
if a[-1] % 2 ** k == 0:
    print(0)
# if the largest number is not a multiple of 2^k, we need to divide it by 2^k
else:
    # we need to find the number of times the largest number can be divided by 2
    # if we divide the largest number by 2 enough times, we can make it a multiple of 2^k
    # we can divide a number by 2 log2(a[-1]) times
    # so, we need to find the number of times we can divide the largest number by 2 until it is a multiple of 2^k
    # we can divide the largest number by 2 log2(a[-1]) times, but we can only divide it by 2 log2(2^k) times
    # since 2^k is a multiple of 2, we can divide the largest number by 2 log2(2^k) times
    # we can divide the largest number by 2 log2(2^k) times, but we need to divide it by 2 log2(a[-1]) times
    # so, we need to divide the largest number by 2 (log2(a[-1]) - log2(2^k)) times
    print(int(log2(a[-1]) - log2(2 ** k)))