
import sys
import heapq
import math
from collections import Counter, deque
from itertools import combinations, permutations, product

sys.setrecursionlimit(10000)

def read_list_int():
    return list(map(int, input().split(' ')))

def read_single_int():
    return int(input())

def read_single_str():
    return input()

def main():
    n = read_single_int()
    s = read_single_str()
    print(s)

if __name__ == '__main__':
    main()
