
n = int(input())

stack_heights = list(map(int, input().split()))

def check_if_sorted(stack_heights):
    for i in range(1, len(stack_heights)):
        prev_stack_height = stack_heights[i-1]
        curr_stack_height = stack_heights[i]
        if curr_stack_height < prev_stack_height:
            return False
    return True

def check_if_can_be_sorted(stack_heights):
    for i in range(1, len(stack_heights)):
        prev_stack_height = stack_heights[i-1]
        curr_stack_height = stack_heights[i]
        if curr_stack_height > prev_stack_height + 1:
            return False
    return True

def check_if_can_be_sorted_in_one_move(stack_heights):
    if max(stack_heights) <= 1:
        return True
    if check_if_sorted(stack_heights):
        return True
    if check_if_can_be_sorted(stack_heights):
        return True
    return False

if check_if_can_be_sorted_in_one_move(stack_heights):
    print("YES")
else:
    print("NO")
