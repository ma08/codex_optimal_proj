
# Read from std in
x, y, x1, y1, x2, y2 = [int(x) for x in input().split()] # split the input into 6 integers.

# Calculate the min distance
min_dist = min(abs(x - x1), abs(x - x2), abs(y - y1), abs(y - y2))

# Print the result
print(min_dist)
