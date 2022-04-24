import math

input_file = open("input.txt", "r")
input = int(input_file.readline())

print(math.floor(math.log(input, 2)))
