

import sys

# Read lines from stdin
lines = [line.strip() for line in sys.stdin]
# Parse input
n = int(lines[0])
recited = [int(line) for line in lines[1:]]

# Find missing numbers
missing = []
for i in range(1, recited[-1] + 1):
    if i not in recited:
        missing.append(i)

# Print results
if len(missing) == 0:
    print("good job")
else:
    for num in missing:
        print(num)
