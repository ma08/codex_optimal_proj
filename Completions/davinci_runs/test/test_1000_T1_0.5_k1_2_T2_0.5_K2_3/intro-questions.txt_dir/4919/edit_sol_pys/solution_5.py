

# # SOLUTION:
# n = int(input())
# d = {}
# for _ in range(n):
#     country, year = input().split()
#     year = int(year)
#     if country in d:
#         d[country].append(year)
#     else:
#         d[country] = [year]
#
# q = int(input())
# for _ in range(q):
#     country, k = input().split()
#     k = int(k)
#     print(sorted(d[country])[k-1])
