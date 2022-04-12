
# Get input from user
A, B, C, D = map(int, input().split()) 

# Calculate areas
area_1 = A * B
area_2 = C * D

# Compare areas and print larger
if area_1 > area_2:
    print(area_1)
elif area_2 > area_1:
    print(area_2)
else:
    print(area_1)
