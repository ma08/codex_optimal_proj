

import math

input = open("input.txt", "r")
input = int(input.readline())
output = math.floor(math.log(input, 2))
output = str(output)
output = open("output.txt", "w")
output.write(output)
