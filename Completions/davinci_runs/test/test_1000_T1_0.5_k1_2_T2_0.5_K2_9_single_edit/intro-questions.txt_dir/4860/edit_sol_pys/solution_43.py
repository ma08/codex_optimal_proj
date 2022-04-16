

import sys
lines = [line.strip() for line in sys.stdin]
n = int(lines[0])
recited = [int(line) for line in lines[1:]]
missing = []
for i in range(1, recited[-1] + 1):
    if i not in recited:
        missing.append(i)
if len(missing) == 0:
    print("good job")
else:
    for num in missing:
        print(num)
