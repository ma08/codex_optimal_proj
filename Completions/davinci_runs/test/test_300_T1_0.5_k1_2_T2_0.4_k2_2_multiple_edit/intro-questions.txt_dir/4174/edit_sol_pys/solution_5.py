import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))[:n]

max_num = max(l)
min_num = min(l)

max_index = l.index(max_num)
min_index = l.index(min_num)

if max_index > min_index:
    print(n - min_index - 1 + max_index)
else:
    print(n - min_index - 1 + max_index - 1)
