import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

print(max(numbers))


# import sys


# def find_max(n, numbers):
#     max_number = 0
#     for i in range(n):
#         if max_number < numbers[i]:
#             max_number = numbers[i]
#     return max_number


# n = int(sys.stdin.readline())
# numbers = list(map(int, sys.stdin.readline().split()))

# print(find_max(n, numbers))
