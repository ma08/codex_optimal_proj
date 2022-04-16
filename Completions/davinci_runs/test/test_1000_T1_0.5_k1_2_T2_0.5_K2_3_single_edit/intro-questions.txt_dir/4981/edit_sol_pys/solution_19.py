

a, b, c = map(int, input().split())  # input()
order = input()
# order = input()
#
if order[0] == 'A':
    if order[1] == 'B':
        if order[2] == 'C':
            print(a, b, c)
        else:
            print(a, c, b)
    else:
        if order[2] == 'B':
            print(b, a, c)
        else:
            print(b, c, a)
else:
    if order[1] == 'A':
        if order[2] == 'B':
            print(c, a, b)
        else:
            print(c, b, a)
    else:
        if order[2] == 'A':
            print(a, c, b)
        else:
            print(b, c, a)

print(a, b, c)

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
#
# print(a, b, c)
