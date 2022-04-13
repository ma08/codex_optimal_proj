


import math

radius, crust = [int(x) for x in input().split()]

whole_area = math.pi * math.pow(radius, 2)

crust_area = math.pi * math.pow(radius - crust, 2)

cheese_area = whole_area - crust_area

print(cheese_area / whole_area * 100)
