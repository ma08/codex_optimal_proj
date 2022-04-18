
# n = int(input())
# days = [int(x) for x in input().split()]

# cleanups = 0
# dirtiness = 0

# for day in days:
#     dirtiness += day
#     if dirtiness >= 20:
#         cleanups += 1
#         dirtiness = 0

# print(cleanups)

# import sys
# sys.stdin = open('input.txt', 'r')

# n = int(input())
# days = [int(x) for x in input().split()]

# cleanups = 0
# dirtiness = 0

# for day in days:
#     dirtiness += day
#     if dirtiness >= 20:
#         cleanups += 1
#         dirtiness = 0

# print(cleanups)

import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

numbers = [int(x) for x in input().split()]

for i in range(m):
    x, y = map(int, input().split())
    print(sum(numbers[x-1:y]))




