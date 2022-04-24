

import math

# a, b, c, d = [int(x) for x in input().split(" ")]

# get the number of integers that can be divisible by c (with no remainder)
# divByC = math.floor(b/c) - math.ceil(a/c) + 1

# get the number of integers that can be divisible by d (with no remainder)
# divByD = math.floor(b/d) - math.ceil(a/d) + 1

# get the number of integers that can be divisible by both c and d (with no remainder)
# divByBoth = math.floor(b/c/d) - math.ceil(a/c/d) + 1

# print(divByC + divByD - divByBoth)


# a, b = [int(x) for x in input().split(" ")]

# for i in range(a, b + 1):
#     print(i, end="")


# a, b = [int(x) for x in input().split(" ")]
# count = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         count += 1
# print(count)


# a, b = [int(x) for x in input().split(" ")]

# sum = 0
# for i in range(a, b + 1):
#     sum += i
# print(sum)


# a, b = [int(x) for x in input().split(" ")]

# for i in range(a, b + 1):
#     if i % 4 == 0 and i % 5 != 0:
#         print(i)


# a, b = [int(x) for x in input().split(" ")]

# for i in range(a, b + 1):
#     if i % 4 == 0 and i % 5 != 0:
#         print(i)


# a, b = [int(x) for x in input().split(" ")]

# for i in range(a, b + 1):
#     print(i, end=" ")


# a, b = [int(x) for x in input().split(" ")]

# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# a, b = [int(x) for x in input().split(" ")]

# for i in range(a, b + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


a, b = [int(x) for x in input().split(" ")]

for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
