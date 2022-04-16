import math


# n = int(input())
#
# max_x = 0
# max_y = 0
#
# for i in range(n):
#     a, b, c = map(int, input().split())
#     x = a / 2
#     y = math.sqrt(c**2 - x**2)
#     if x > max_x:
#         max_x = x
#     if y > max_y:
#         max_y = y
#
# print(max_x + max_y)

a = int(input())

for i in range(1, a + 1):
    if a % i == 0:
        print(i)

# n = int(input())
#
# for i in range(n):
#     a, b, c = map(int, input().split())
#     if a + b == c:
#         print('YES')
#     else:
#         print('NO')
