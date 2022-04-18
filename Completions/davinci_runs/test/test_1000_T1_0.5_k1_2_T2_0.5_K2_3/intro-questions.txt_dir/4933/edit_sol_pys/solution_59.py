

#SOLUTION 1

# a, b, c = [int(x) for x in input().split()]

# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if a > b:
#     a, b = b, a

# d = a + c - b
# print(d)

#SOLUTION 2

a, b, c = sorted([int(x) for x in input().split()])

print(a + c - b)
