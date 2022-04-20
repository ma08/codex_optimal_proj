

import sys
import re
import math
import string
import itertools
import collections
import bisect
import queue
import heapq
import time
import random
import copy

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7


def inp(): return int(sys.stdin.readline())


def inp_list(): return list(map(int, sys.stdin.readline().split()))


def lcm(x, y): return (x * y) // math.gcd(x, y)
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False
    return prime


def eratosthenes_sieve(n):
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime


def get_primes(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


def prime_factor(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def perm(n, r):
    return math.factorial(n) // math.factorial(n - r)


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5




def comb(n, r): return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def perm(n, r): return math.factorial(n) // math.factorial(n - r)


def dist(x1, y1, x2, y2): return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def func(n, m, k):
    pass


func(inp(), inp(), inp())
