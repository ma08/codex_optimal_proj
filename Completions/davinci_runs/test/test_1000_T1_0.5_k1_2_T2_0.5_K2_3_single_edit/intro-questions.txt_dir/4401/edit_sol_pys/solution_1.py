#!/usr/bin/python3

# Swap the contents of the boxes A and B
# Swap the contents of the boxes A and C

x, y, z = map(int, input().split())  # take input as space separated integers

# using list
box = [x, y, z]  # create a list
box[0], box[1] = box[1], box[0]
box[0], box[2] = box[2], box[0]
print(box[0], box[1], box[2])

# using variable
x, y, z = y, z, x
print(x, y, z)
