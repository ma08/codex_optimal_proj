
from math import factorial as f
from sys import stdin

def choose(n, k):
    return f(n) / (f(k) * f(n - k))

def p(n):
    return sum(choose(n, i) / n**i for i in range(n))

print(p(int(stdin.readline())))
