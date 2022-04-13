#test
# a, b, c = map(int, input().split())
# order = input()

# if order[0] == 'A':
#     if a > b:
#         a, b = b, a
#     if b > c:
#         b, c = c, b
#         if a > b:
#             a, b = b, a
# elif order[0] == 'B':
#     if b > a:
#         b, a = a, b
#     if b > c:
#         b, c = c, b
#         if a > b:
#             a, b = b, a
# elif order[0] == 'C':
#     if c > a:
#         c, a = a, c
#     if c > b:
#         c, b = b, c
#         if a > b:
#             a, b = b, a

# print(a, b, c)

# a = int(input())
# b = int(input())
# c = int(input())

# if a < b:
#     a, b = b, a
# if b < c:
#     b, c = c, b
# if a < b:
#     a, b = b, a

# print(a, b, c)

# a = int(input())
# b = int(input())
# c = int(input())

# if a < b:
#     a, b = b, a
#     if a < c:
#         a, c = c, a
#     if b < c:
#         b, c = c, b
# else:
#     if a < c:
#         a, c = c, a
#     if b < c:
#         b, c = c, b

# print(a, b, c)

# a = int(input())
# b = int(input())
# c = int(input())

# if a < b:
#     a, b = b, a
#     if a < c:
#         a, c = c, a
#     if b < c:
#         b, c = c, b
# else:
#     if a < c:
#         a, c = c, a
#     if b < c:
#         b, c = c, b

# print(a, b, c)

a = int(input())
b = int(input())
c = int(input())

if a < b:
    a, b = b, a
    if a < c:
        a, c = c, a
        if b < c:
            b, c = c, b
    else:
        if b < c:
            b, c = c, b
else:
    if a < c:
        a, c = c, a
        if b < c:
            b, c = c, b
    else:
        if b < c:
            b, c = c, b

print(a, b, c)
