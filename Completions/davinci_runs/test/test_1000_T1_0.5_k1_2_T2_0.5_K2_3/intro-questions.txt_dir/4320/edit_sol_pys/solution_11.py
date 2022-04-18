
import sys

# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Since the first line is the number of test cases,
# we're going to iterate through the rest of the lines.
for i in range(1, len(lines)):
    # Get the number of elements.
    n = int(lines[i])

    # 
    print(int(n/2) + 1)
    
