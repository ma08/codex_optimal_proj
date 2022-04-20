

# get number of squares
n = int(input())

# get heights of each square
heights = [int(x) for x in input().split()]

# store the current max height
max_height = 0

# store the number of times we can move
num_moves = 0

# iterate through the heights
for height in heights:

    # if the height is less than the current max height
    if height < max_height:

        # increment the number of moves
        num_moves += 1

    # else, the height is greater than the current max height
    else:

        # update the max height
        max_height = height

# print the number of moves
print(num_moves)