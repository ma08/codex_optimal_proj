

"""
This is a simulation problem.
"""

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def simulate(arr):
    stack_arr = [[x] for x in arr]
    sorted_arr = []
    while len(stack_arr) > 0:
        # find the tallest stack
        tallest_stack = stack_arr[0]
        tallest_stack_idx = 0
        for i in range(1, len(stack_arr)):
            if len(stack_arr[i]) > len(tallest_stack):
                tallest_stack = stack_arr[i]
                tallest_stack_idx = i
        # remove the tallest stack
        sorted_arr.append(len(tallest_stack))
        stack_arr.pop(tallest_stack_idx)
        # shift the remaining stacks to the left
        for i in range(len(stack_arr)):
            if len(stack_arr[i]) > 0 and len(stack_arr[i]) < len(stack_arr[i - 1]):
                stack_arr[i - 1].append(stack_arr[i].pop())
    return sorted_arr

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    if is_sorted(simulate(arr)):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()