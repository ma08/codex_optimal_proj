import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(10000)

# Debug output
def chkprint(*args):
    names = {id(v):k for k,v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

# Binary converter
def to_bin(x):
    return bin(x)[2:]

# Set 2 dimension list
def dim2input(N):
    li = []
    for _ in range(N):
        li.append(input().split())
    return li


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

print(min(a//g, b//g, c//g)*7)
