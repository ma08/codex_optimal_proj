

import math, sys

infile = open("input.txt", "r")
outfile = open("output.txt", "w")

input = int(infile.readline())

outfile.write(str(math.floor(math.log(input, 2))))
