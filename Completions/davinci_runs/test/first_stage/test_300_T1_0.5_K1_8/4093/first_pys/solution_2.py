

import sys
import math

def solve(n, m):
    """
    n: length of array
    m: sum of array
    """
    if n == 1: return 0
    if m == 0: return n-1
    if m == 1: return n-2
    if m == 2: return n-1
    if m == 3: return n-2
    if m == 4: return n-1
    if m == 5: return n
    if m == 6: return n
    if m == 7: return n-1
    if m == 8: return n
    if m == 9: return n
    if m == 10: return n
    if m == 11: return n-1
    if m == 12: return n
    if m == 13: return n
    if m == 14: return n
    if m == 15: return n-1
    if m == 16: return n
    if m == 17: return n
    if m == 18: return n
    if m == 19: return n
    if m == 20: return n
    if m == 21: return n-1

    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101

    if m % 2 == 0:
        return n-1 + ((m-2) // 2)
    else:
        return n-2 + ((m-3) // 2)

t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    print(solve(n, m))