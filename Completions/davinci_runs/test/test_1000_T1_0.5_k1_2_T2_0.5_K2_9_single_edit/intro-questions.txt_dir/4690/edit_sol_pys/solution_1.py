
# Get input
A, B, C, D = map(int, input().split()) # space seperated input

# Calculate areas
area_1 = A * B # area of rectangle 1
area_2 = C * D # area of rectangle 2

# Compare areas and print larger
if area_1 > area_2:
    print(area_1) # print area of rectangle 1
elif area_2 > area_1:
    print(area_2) # print area of rectangle 2
else:
    print(area_1) # print area of rectangle 1 or 2
