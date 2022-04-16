
# Get input
A, B, C, D = map(int, input().split())

# Calculate areas
area_1 = A * B
area_2 = C * D

# Compare areas and print larger
print(max(area_1, area_2))
