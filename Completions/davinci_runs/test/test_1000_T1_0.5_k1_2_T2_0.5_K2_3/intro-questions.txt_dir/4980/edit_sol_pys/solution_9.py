

import sys

n = int(sys.stdin.readline())

pink_count = 0
for i in range(n):
    line = sys.stdin.readline()
    if "pink" in line.lower():
        pink_count += 1

if pink_count == 0:
    print("I must watch Star Wars with my daughter.")
else:
    print(pink_count)
