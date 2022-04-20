

# Get input from user
H, W = map(int, input().split()) # H: height, W: width
h, w = map(int, input().split()) # h: height, w: width

# Calculate number of white cells
print((H-h)*(W-w))
