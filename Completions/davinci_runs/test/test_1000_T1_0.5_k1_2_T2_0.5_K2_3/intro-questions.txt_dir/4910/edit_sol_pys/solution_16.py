
import math
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

num_cases = int(lines[0])

for i in range(num_cases):
    case = lines[i + 1]
    case = case.split()
    case = [int(i) for i in case]
    case = sorted(case)
    print(math.sqrt((case[0]**2) + (case[1]**2)))
