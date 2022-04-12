#
# # SOLUTION
#
# n = int(input())
#
# d = {}
#
# for i in range(n):
#     country, year = input().split()
#     year = int(year)
#     if country not in d:
#         d[country] = []
#     d[country].append(year)
#
# q = int(input())
#
# for i in range(q):
#     country, k = input().split()
#     k = int(k)
#     print(d[country][k-1])
