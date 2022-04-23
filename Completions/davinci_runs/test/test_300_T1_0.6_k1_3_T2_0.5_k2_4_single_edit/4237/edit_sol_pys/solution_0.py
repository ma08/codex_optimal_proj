
import math

a, b, c, d = [int(x) for x in input().split(" ")] 

# get the number of integers that can be divisible by c (with no remainder)
divByC = math.floor(b/c) - math.ceil(a/c) + 1 

# get the number of integers that can be divisible by d (with no remainder)
divByD = math.floor(b/d) - math.ceil(a/d) + 1 

# get the number of integers that can be divisible by both c and d (with no remainder)
divByBoth = math.floor(b/c/d) - math.ceil(a/c/d) + 1 

print(divByC + divByD - divByBoth) 
