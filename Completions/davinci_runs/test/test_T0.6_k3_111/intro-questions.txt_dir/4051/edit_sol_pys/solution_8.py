

n = int(input())

stack_heights = list(map(int, input().split()))[:n]

if max(stack_heights) <= 1:
    print("YES")
    exit()

# check if the array can be sorted (i.e. all the heights are 1 or 2)
for i in range(1, n):
    prev_stack_height = stack_heights[i-1]
    curr_stack_height = stack_heights[i]
    if curr_stack_height > prev_stack_height + 1:
        print("NO")
        exit()

# if it can, then check if it is already sorted (i.e. all the heights are 1)
for i in range(1, n):
    prev_stack_height = stack_heights[i-1]
    curr_stack_height = stack_heights[i]
    if curr_stack_height < prev_stack_height:
        print("NO")
        exit()

print("YES")
