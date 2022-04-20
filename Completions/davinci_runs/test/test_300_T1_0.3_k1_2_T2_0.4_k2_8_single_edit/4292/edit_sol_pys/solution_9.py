# coding: utf-8

# input
N, K = map(int, input().split())
p = [int(i) for i in input().split()]

# sort
p.sort()

# output
print(sum(p[:K]))
