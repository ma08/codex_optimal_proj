import sys, math

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

print(min(lst), max(lst))
