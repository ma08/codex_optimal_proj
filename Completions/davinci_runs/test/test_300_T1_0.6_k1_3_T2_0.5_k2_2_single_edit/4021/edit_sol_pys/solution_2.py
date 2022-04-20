

import sys
import math

input_file = open("input.txt", "r")
input = int(input_file.readline())

sys.stdout.write(str(math.floor(math.log(input, 2))))
