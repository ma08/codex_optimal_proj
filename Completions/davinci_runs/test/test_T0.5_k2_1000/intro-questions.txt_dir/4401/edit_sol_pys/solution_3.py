
# Swap the contents of the boxes x and y
# Swap the contents of the boxes x and z

x, y, z = map(int, input().split())

# using list
box = [x, y, z]
box[0], box[1] = box[1], box[0]
box[0], box[2] = box[2], box[0]
print(box[0], box[1], box[2])

# using variable
x, y, z = y, z, x
print(x, y, z)
