

# import math

# input = open("input.txt", "r")
# input = int(input.readline())

# print(math.floor(math.log(input, 2)))

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# print(fib(10))

# def fib_rec(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_rec(n - 1) + fib_rec(n - 2)

# print(fib_rec(20))

# def fib_memo(n, memo):
#     if memo[n] is not None:
#         return memo[n]
#     if n == 1 or n == 2:
#         result = 1
#     else:
#         result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
#     memo[n] = result
#     return result

# def fib_memo_wrapper(n):
#     memo = [None] * (n + 1)
#     return fib_memo(n, memo)

# print(fib_memo_wrapper(20))

# def fib_bottom_up(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up = [None] * (n + 1)
#     bottom_up[1] = 1
#     bottom_up[2] = 1
#     for i in range(3, n + 1):
#         bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
#     return bottom_up[n]

# print(fib_bottom_up(20))

# def fib_bottom_up_space_efficient(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient(20))

# def fib_bottom_up_space_efficient_2(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient_2(20))

# def fib_bottom_up_space_efficient_3(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient_3(20))

# def fib_bottom_up_space_efficient_4(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient_4(20))

# def fib_bottom_up_space_efficient_5(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient_5(20))

# def fib_bottom_up_space_efficient_6(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient_6(20))

# def fib_bottom_up_space_efficient_7(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient_7(20))

# def fib_bottom_up_space_efficient_8(n):
#     if n == 1 or n == 2:
#         return 1
#     bottom_up_2 = 1
#     bottom_up_1 = 1
#     for _ in range(3, n + 1):
#         bottom_up = bottom_up_1 + bottom_up_2
#         bottom_up_2 = bottom_up_1
#         bottom_up_1 = bottom_up
#     return bottom_up

# print(fib_bottom_up_space_efficient_8(20))
