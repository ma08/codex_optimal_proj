
import sys
from collections import deque
from functools import reduce
import math
sys.setrecursionlimit(10**7)

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,k = get_nums_l()
a = get_nums_l()

print(a)
