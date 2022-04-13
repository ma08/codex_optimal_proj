# coding: utf-8

N, P, Q = [int(x) for x in input().split()]

if P % (N + 1) == 0 or Q % (N + 1) == 0:
    print("opponent")
else:
    print("paul")
