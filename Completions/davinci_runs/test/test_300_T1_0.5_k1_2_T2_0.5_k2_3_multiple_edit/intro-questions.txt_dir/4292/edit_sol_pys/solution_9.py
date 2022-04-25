import sys

n, k = map(int, sys.stdin.readline().split())  # number of elements, number of elements to select
p = list(map(int, sys.stdin.readline().split()))  # list of elements

print(sum(sorted(p)[:k]))
