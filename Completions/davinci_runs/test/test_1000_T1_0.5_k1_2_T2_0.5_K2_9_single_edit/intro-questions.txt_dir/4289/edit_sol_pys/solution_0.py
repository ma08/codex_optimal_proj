
import math
import sys

input = sys.stdin.readline

n = int(input())
t, a = map(int, input().split())
h = [int(input()) for i in range(n)]

print(math.ceil(sum(h) / n))
