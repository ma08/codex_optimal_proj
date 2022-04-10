
n = int(input())

stack_heights = list(map(int, input().split()))

if max(stack_heights) <= 1:
    print("YES")
    exit()

# check if the array can be sorted in one move
for i in range(1, len(stack_heights)):
    prev_stack_height = stack_heights[i-1]
    curr_stack_height = stack_heights[i]
    if curr_stack_height > prev_stack_height + 1:
        print("NO")
        exit()

# if it can, then check if it is already sorted
for i in range(1, len(stack_heights)):
    prev_stack_height = stack_heights[i-1]
    curr_stack_height = stack_heights[i]
    if curr_stack_height < prev_stack_height:
        print("NO")
        exit()

print("YES")
