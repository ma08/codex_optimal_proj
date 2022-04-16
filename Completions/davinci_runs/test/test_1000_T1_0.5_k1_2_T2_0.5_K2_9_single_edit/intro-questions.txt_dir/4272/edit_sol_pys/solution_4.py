import sys
from collections import defaultdict
import numpy as np
import math
import itertools


sys.setrecursionlimit(1000000)
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))
read_list_str = lambda: list(map(str, sys.stdin.readline().strip().split(' ')))

for i in range(n - 2):
    if s[i] == "A" and s[i + 1] == "B" and s[i + 2] == "C":
        count += 1

print(count)
