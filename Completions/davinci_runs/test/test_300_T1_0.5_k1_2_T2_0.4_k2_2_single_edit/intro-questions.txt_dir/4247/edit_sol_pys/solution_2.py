

# n = int(input())
# p = [int(x) for x in input().split()]

# count = 0
# for i in range(1, n - 1):
#     if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
#         count += 1

# print(count)

import math

n = int(input())
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]


def distance(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


total = 0
for i in range(n):
    for j in range(i + 1, n):
        total += distance(x[i], x[j])
        total += distance(y[i], y[j])

print(total / n)
