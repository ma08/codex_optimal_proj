import sys
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines



n = int(input())
x = list(map(int, input().split()))

x_min = min(x)
x_max = max(x)

x_sum = sum(x)

x_min_sum = sum([(i - x_min) ** 2 for i in x])
x_max_sum = sum([(i - x_max) ** 2 for i in x])
x_sum_sum = sum([(i - x_sum / n) ** 2 for i in x])

print(int(min(x_min_sum, x_max_sum, x_sum_sum)))
