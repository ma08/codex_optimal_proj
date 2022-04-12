# coding: utf-8

n = int(input())
d = {}
for i in range(n):
    s, p = input().split() # s: subject, p: point
    p = int(p) # convert str to int
    if s not in d.keys():
        d[s] = [p] # create a new list
    else:
        d[s].append(p) # add the point to the list

for s in sorted(d.keys()):
    d[s].sort(reverse=True) # sort in descending order

for s in sorted(d.keys()):
    for p in d[s]: # print out the points
        print(p)
