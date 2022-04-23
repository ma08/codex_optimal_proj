#!/usr/bin/env python3

# read N
N = int(input())
# read list
L = list(map(int, input().split()))

# create dictionary for numbers and count
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1

# create list of odd numbers and count
X = []
for i in D:
    if D[i] % 2:
        X.append(i)

# print odd numbers
print(X[0], X[1])
