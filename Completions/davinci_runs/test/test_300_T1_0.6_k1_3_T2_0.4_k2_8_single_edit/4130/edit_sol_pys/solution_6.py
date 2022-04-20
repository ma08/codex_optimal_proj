
import sys
lines = sys.stdin.readlines()

n = int(lines[0])
weights = [int(i) for i in lines[1].split()]
weights.sort()
count = 1
prev = weights[0]
for i in range(1, n):
  if weights[i] != prev:
    count += 1
  prev = weights[i]

print(count)
