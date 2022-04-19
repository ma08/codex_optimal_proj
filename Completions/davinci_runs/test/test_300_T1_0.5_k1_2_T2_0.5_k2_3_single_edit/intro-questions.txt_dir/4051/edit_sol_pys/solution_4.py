

n = int(input())
arr = list(map(int, input().split()))

def sort_ravioli(lst):
    sorted_lst = []
    stack = []
    for i in range(len(lst)):
        stack.append(lst[i])
    while len(stack) > 0:
        tallest_stack = max(stack)
        tallest_stack_index = stack.index(tallest_stack)
        sorted_lst.append(tallest_stack)
        del stack[tallest_stack_index]
    return sorted_lst

def check_ravioli_sort(arr):
    if sort_ravioli(arr) == sorted(arr):
        return "YES"
    else:
        return "NO"

print(check_ravioli_sort(arr))
