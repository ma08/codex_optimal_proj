
from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import ceil,log
from fractions import gcd
int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7


def main():
    t = int_input()
    for i in range(t):
        a, b, x, y, n = multi_int_input()
        if a == x:
            b = max(y, b - n)
        elif b == y:
            a = max(x, a - n)
        else:
            n1 = n
            a1 = a
            b1 = b
            while n > 0 and a > x and b > y:
                if a - x > b - y:
                    a -= 1
                    n -= 1
                else:
                    b -= 1
                    n -= 1
            if n > 0:
                if a > x:
                    a -= n
                else:
                    b -= n
            a = max(x, a)
            b = max(y, b)
            n1 -= n
            a1 = max(x, a1 - n1)
            b1 = max(y, b1 - n1)
            print(min(a * b, a1 * b1))


if __name__ == '__main__':
    main()
