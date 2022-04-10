

import sys

n = int(input())

prefixes = []
suffixes = []

for i in range(2*n-2):
  s = input()
  if len(s) == 1:
    prefixes.append(s)
  elif len(s) == n-1:
    suffixes.append(s)

prefixes.sort()
suffixes.sort()

for i in range(n-1):
  if prefixes[i][0] == suffixes[i][0]:
    sys.stdout.write("P")
  else:
    sys.stdout.write("S")

print("")