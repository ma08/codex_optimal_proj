

import sys
import math

lines = sys.stdin.readlines()

radius, crust = [float(x) for x in lines[0].split()]

# area of the whole pizza
whole_area = math.pi * math.pow(radius, 2)
# area of the crust
crust_area = math.pi * math.pow(radius - crust, 2)

# subtract the area of the crust from the whole area
# to get the area of the cheese
cheese_area = whole_area - crust_area

# divide the area of the cheese by the whole area
# and multiply by 100 to get the percentage of the pizza
# that has cheese
print(cheese_area / whole_area * 100)
