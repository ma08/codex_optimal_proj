
import math
import itertools
import numpy as np
import sys
sys.setrecursionlimit(10**6)
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a
def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, gcd(a_list[i], a_list[j]))
    print(ans)
if __name__ == '__main__':
    main()
