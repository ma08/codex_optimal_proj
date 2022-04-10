

import sys

input = sys.stdin.readline().strip()

operands = input.split("+")

for i in range(len(operands)):
    operands[i] = operands[i].split("-")
    if len(operands[i]) == 1:
        operands[i] = int(operands[i][0])
    else:
        operands[i][0] = int(operands[i][0])
        operands[i][1] = int(operands[i][1])
        operands[i] = operands[i][0] - operands[i][1]

print(sum(operands))