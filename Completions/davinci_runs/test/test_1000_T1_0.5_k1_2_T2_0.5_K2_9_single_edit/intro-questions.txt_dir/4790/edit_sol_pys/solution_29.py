

import sys
import math

#get the number of rows and columns
rows, columns = [int(x) for x in input().split()]

#get the first row
row = input()

#get the number of black and white stones
b = row.count('B')
w = row.count('W')

#calculate the number of swaps needed
swaps = math.ceil(b / 2) + math.ceil(w / 2)

#output the number of swaps
print(swaps)
