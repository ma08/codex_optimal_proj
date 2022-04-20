

from math import gcd
from functools import reduce
from collections import defaultdict

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_list(l):
    return reduce(lcm, l)

def naive_lcm_pair(a):
    lcm_min = lcm_list(a)
    pair = None
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            lcm_curr = lcm(a[i], a[j])
            if lcm_curr < lcm_min:
                lcm_min = lcm_curr
                pair = (i + 1, j + 1)
    return pair

def fast_lcm_pair(a):
    lcm_min = lcm_list(a)
    pair = None
    factors = defaultdict(int)
    for x in a:
        for f in range(2, x + 1):
            if x % f == 0:
                factors[f] += 1
    for i in range(len(a)):
        for f in range(2, a[i] + 1):
            if a[i] % f == 0:
                factors[f] -= 1
                if factors[f] == 0:
                    del factors[f]
                for j in range(i + 1, len(a)):
                    lcm_curr = lcm(a[i], a[j])
                    if lcm_curr < lcm_min:
                        lcm_min = lcm_curr
                        pair = (i + 1, j + 1)
                factors[f] += 1
    return pair

def main():
    _ = int(input())
    a = list(map(int, input().split()))
    print(*fast_lcm_pair(a))

if __name__ == '__main__':
    main()