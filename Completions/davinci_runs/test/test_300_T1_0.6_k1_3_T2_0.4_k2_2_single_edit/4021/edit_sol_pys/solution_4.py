

import math

input_file = open("input.txt", "r")
input_file = int(input_file.readline())

print(math.floor(math.log(input_file, 2)))
