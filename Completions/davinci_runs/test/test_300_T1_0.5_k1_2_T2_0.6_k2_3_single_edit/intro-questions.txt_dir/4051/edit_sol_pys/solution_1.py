
import sys

def sort_ravioli(arr):
    sorted_stacks = []
    stack_heights = []

    for stack in arr:
        stack_heights.append(stack)

    while len(stack_heights) > 0:
        tallest_stack = max(stack_heights)
        tallest_stack_index = stack_heights.index(tallest_stack)
        sorted_stacks.append(tallest_stack)
        del stack_heights[tallest_stack_index]

    return sorted_stacks


def check_ravioli_sort(arr):
    if sort_ravioli(arr) == sorted(arr):
        return "YES"
    else:
        return "NO"
