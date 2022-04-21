from collections import defaultdict


# n = int(input())
# a = list(map(int, input().split()))
#
# a.sort()
#
# count = 1
# for i in range(1, n):
#     if a[i] != a[i-1]:
#         count += 1
#
# print(count)

# n = int(input())
# a = list(map(int, input().split()))
#
# a.sort()
#
# count = 1
# for i in range(1, n):
#     if a[i] != a[i-1]:
#         count += 1
#
# print(count)

# n = int(input())
# a = list(map(int, input().split()))
#
# a.sort()
#
# count = 1
# for i in range(1, n):
#     if a[i] != a[i-1]:
#         count += 1
#
# print(count)

# n = int(input())
# a = list(map(int, input().split()))
#
# a.sort()
#
# count = 1
# for i in range(1, n):
#     if a[i] != a[i-1]:
#         count += 1
#
# print(count)

n = int(input())
a = list(map(int, input().split()))

dict = defaultdict(int)
for x in a:
    dict[x] += 1

count = len(dict)

print(count)
