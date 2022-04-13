
import sys

inputs = sys.stdin.readline().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

sum = a + b + c

print(sum - 9 * ((sum - 1) // 9))
