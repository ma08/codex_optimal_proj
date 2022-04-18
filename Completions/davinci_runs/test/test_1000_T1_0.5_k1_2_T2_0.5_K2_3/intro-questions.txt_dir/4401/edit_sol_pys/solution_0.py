
# Swap the contents of the boxes A and B.
# Swap the contents of the boxes A and C.

x, y, z = map(int, input().split())  # input

# using list
box = [x, y, z]  # list
box[0], box[1] = box[1], box[0]  # swap
box[0], box[2] = box[2], box[0]  # swap
print(box[0], box[1], box[2])

# using variables
x, y, z = y, z, x  # swap
print(x, y, z)
