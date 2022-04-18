
n = int(input())
d = {}
for i in range(n):
    s, p = input().split()  # s = subject, p = point
    p = int(p)  # convert string to int
    if s not in d.keys():
        d[s] = [p]  # create new key and assign list
    else:
        d[s].append(p)  # append new point to the list

for s in sorted(d.keys()):
    d[s].sort(reverse=True)  # sort each list in descending order

for s in sorted(d.keys()):
    for p in d[s]:  # print all points in each list
        print(p)  # print each point

print(d)
