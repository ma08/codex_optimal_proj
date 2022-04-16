

n = int(input())
grid = []
for i in range(n):
    grid.append(input())

def check_row(row):
    color = row[0]
    count = 0
    for i in range(n):
        if row[i] == color:
            count += 1
        else:
            color = row[i]
            count = 1
        if count == 3:
            return False
    return True

def check_column(column):
    color = column[0]
    count = 0
    for i in range(n):
        if column[i] == color:
            count += 1
        else:
            color = column[i]
            count = 1
        if count == 3:
            return False
    return True

def check_grid():
    for i in range(n):
        if not check_row(grid[i]):
            return False
        column = ""
        for j in range(n):
            column += grid[j][i]
        if not check_column(column):
            return False
    return True

if check_grid():
    print(1)
else:
    print(0)

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the countApplesAndOranges function below.
# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     num_apples = 0
#     num_oranges = 0
#     for i in range(len(apples)):
#         if s <= a + apples[i] <= t:
#             num_apples += 1
#     for i in range(len(oranges)):
#         if s <= b + oranges[i] <= t:
#             num_oranges += 1
#     print(num_apples)
#     print(num_oranges)

# if __name__ == '__main__':
#     st = input().split()

#     s = int(st[0])

#     t = int(st[1])

#     ab = input().split()

#     a = int(ab[0])

#     b = int(ab[1])

#     mn = input().split()

#     m = int(mn[0])

#     n = int(mn[1])

#     apples = list(map(int, input().rstrip().split()))

#     oranges = list(map(int, input().rstrip().split()))

#     countApplesAndOranges(s, t, a, b, apples, oranges)
