
# Get input
H, W = map(int, input().split())
h, w = map(int, input().split())

# Calculate number of black cells
print((H-h)*(W-w))
