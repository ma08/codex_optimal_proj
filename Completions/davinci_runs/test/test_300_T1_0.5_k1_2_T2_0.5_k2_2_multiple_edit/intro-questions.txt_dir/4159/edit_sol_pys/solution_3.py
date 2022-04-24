#!/usr/bin/python3


# a,b,k = map(int, input().split())
#
# if k <= a:
#     a -= k
# else:
#     k -= a
#     a = 0
#     if k <= b:
#         b -= k
#     else:
#         b = 0
#
# print(a,b)

a, b, k = map(int, input().split())

for i in range(k):
    if i % 2 == 0:
        a //= 2
    else:
        b //= 2

print(a, b)
