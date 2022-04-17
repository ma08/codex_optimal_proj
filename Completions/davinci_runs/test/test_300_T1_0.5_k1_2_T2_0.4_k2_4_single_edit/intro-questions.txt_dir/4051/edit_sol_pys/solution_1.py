

import sys

# n = int(input())
# arr = list(map(int, input().split()))

def sort_ravioli(n, arr):
    if n == 1:
        return "YES"
    else:
        sorted_array = []
        stacks = []
        for i in range(len(arr)):
            stacks.append(arr[i])
        while len(stacks) > 0:
            tallest_stack = max(stacks)
            tallest_stack_index = stacks.index(tallest_stack)
            sorted_array.append(tallest_stack)
            del stacks[tallest_stack_index]
        if sorted_array == sorted(arr):
            return "YES"
        else:
            return "NO"

# def check_ravioli_sort(arr):
#     if sort_ravioli(arr) == sorted(arr):
#         return "YES"
#     else:
#         return "NO"

# print(check_ravioli_sort(arr))

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sort_ravioli(n, arr))
