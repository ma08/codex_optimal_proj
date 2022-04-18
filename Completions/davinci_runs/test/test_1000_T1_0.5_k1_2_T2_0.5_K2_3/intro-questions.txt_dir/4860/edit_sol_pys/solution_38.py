
import sys

lines = [line.strip() for line in sys.stdin] # Read lines from stdin

n = int(lines[0]) # Parse input
recited = [int(line) for line in lines[1:]] 

missing = [] # Find missing number
for i in range(1, recited[-1] + 1):
    if i not in recited:
        missing.append(i)

if len(missing) == 0: # Print results
    print("good job")
else:
    for num in missing:
        print(num)
