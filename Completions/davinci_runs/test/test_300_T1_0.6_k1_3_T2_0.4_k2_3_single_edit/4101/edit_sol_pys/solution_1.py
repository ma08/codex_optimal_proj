


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

r = []
c = []
for i in range(n):
    r.append(0)
for j in range(m):
    c.append(0)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            r[i] = (r[i] + 1) % 2
            c[j] = (c[j] + 1) % 2

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            r[i] = (r[i] + 1) % 2
            c[j] = (c[j] + 1) % 2

a_sort = []
for i in range(n):
    for j in range(m):
        a_sort.append(a[i][j])
a_sort = sorted(a_sort)

for i in range(n):
    for j in range(m):
        if a[i][j] != a_sort[i * m + j]:
            print("NO")
            exit()

print("YES")
print("".join(map(str, r)))
print("".join(map(str, c)))
#!/usr/bin/env python

# import sys
# from math import *
# from string import *
# from datetime import *
# from time import *
# from random import *

# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a.append(list(map(int, input().split())))

# #print(n, m)
# #print(a)

# r = []
# c = []
# for i in range(n):
#     r.append(0)
# for j in range(m):
#     c.append(0)

# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             r[i] = (r[i] + 1) % 2
#             c[j] = (c[j] + 1) % 2

# #print(r)
# #print(c)

# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 1:
#             r[i] = (r[i] + 1) % 2
#             c[j] = (c[j] + 1) % 2

# #print(r)
# #print(c)

# a_sort = []
# for i in range(n):
#     for j in range(m):
#         a_sort.append(a[i][j])
# a_sort = sorted(a_sort)
# #print(a_sort)

# for i in range(n):
#     for j in range(m):
#         if a[i][j] != a_sort[i * m + j]:
#             print("NO")
#             exit()

# print("YES")
# print("".join(map(str, r)))
# print("".join(map(str, c)))
