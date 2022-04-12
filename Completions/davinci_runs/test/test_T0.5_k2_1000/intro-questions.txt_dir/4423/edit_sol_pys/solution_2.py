# coding: utf-8

n = int(input())
d = {}
for i in range(n):
    s, p = input().split()  # s: subject, p: point
    p = int(p)  # convert str to int
    if s not in d.keys():
        d[s] = [p]  # d[s] is a list
    else:
        d[s].append(p)  # append p to the list d[s]

for s in sorted(d.keys()):
    d[s].sort(reverse=True)  # sort the list d[s] in descending order

for s in sorted(d.keys()):
    for p in d[s]:
        print(p)  # print each element in the list d[s]
