
from collections import Counter

s = input()
t = input()

def solve(s, t):
    for i in range(len(s)):
        if s[i] != t[2*i]:
            print(s[i], end='')

def solve2(s, t):
    s_counter = Counter(s)
    t_counter = Counter(t)
    for k, v in s_counter.items():
        if v != t_counter[k]:
            print(k * v, end='')

solve2(s, t)
