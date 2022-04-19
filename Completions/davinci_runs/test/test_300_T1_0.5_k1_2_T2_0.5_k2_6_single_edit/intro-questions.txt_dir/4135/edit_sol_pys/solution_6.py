

import sys

file = open(sys.argv[1], "r")

for line in file:
    line = line.strip()
    if line == "":
        continue

    print(line)
