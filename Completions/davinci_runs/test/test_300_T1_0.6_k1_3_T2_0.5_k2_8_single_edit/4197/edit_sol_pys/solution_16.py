#!/usr/bin/python3


n = int(input())  # number of elements in the array
a = list(map(int, input().split()))  # array

l = [0] * n  # list to store the result

for i in range(n):
    l[a[i]-1] = i+1

for i in l:
    print(i)
