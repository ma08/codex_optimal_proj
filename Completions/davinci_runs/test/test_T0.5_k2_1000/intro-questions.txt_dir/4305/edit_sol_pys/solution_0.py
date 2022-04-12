
h, a = map(int, input().split()) # h is height, a is angle
print((h-1)//a + 1) # (h-1)//a is the number of times the ladder can be lowered, +1 is for the last time
