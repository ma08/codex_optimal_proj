
import sys

n = int(input())
arr = list(map(int, input().split()))

def sort_raviolis(arr):
    sorted_array = []
    stacks = []
    for i in range(len(arr)):
        stacks.append(arr[i])
    while len(stacks) > 0:
        tallest_stack = max(stacks)
        tallest_stack_index = stacks.index(tallest_stack)
        sorted_array.append(tallest_stack)
        del stacks[tallest_stack_index]
    return sorted_array

def check_raviolis_sort(arr):
    if sort_raviolis(arr) == sorted(arr):
        return "YES"
    else:
        return "NO"

print(check_raviolis_sort(arr))
