

import sys
import math

n = int(sys.stdin.readline().strip())

for line in sys.stdin:
    line = line.strip()
    if len(line) == 1:
        print("Yes")
        continue
    if len(line) != len(set(line)):
        print("No")
        continue
    if ord(line[0]) - ord(line[1]) == -1 or ord(line[0]) - ord(line[1]) == 1:
        print("Yes")
        continue
    print("No")