
import sys
import math

lines = sys.stdin.readlines()

radius, crust = [int(x) for x in lines[0].split()] # split the input line into 2 ints

# area of the whole pizza
whole_area = math.pi * math.pow(radius, 2) # pi * r * r
# area of the crust
crust_area = math.pi * math.pow(radius - crust, 2) # pi * (r - c) * (r - c)

# subtract the area of the crust from the whole area
# to get the area of the cheese
cheese_area = whole_area - crust_area # whole - crust = cheese

# divide the area of the cheese by the whole area
# and multiply by 100 to get the percentage of the pizza
# that has cheese
print(cheese_area / whole_area * 100) # cheese / whole * 100
