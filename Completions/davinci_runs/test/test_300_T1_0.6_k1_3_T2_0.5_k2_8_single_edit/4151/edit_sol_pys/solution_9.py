
import math
# SOLUTION

n = int(input())
a = list(map(int, input().split()))

d = {}

for i in a:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

if len(d) == 1 and d[list(d.keys())[0]] == 1:
  print(0)
  quit()

if len(d) == 1 and d[list(d.keys())[0]] > 1:
  print(math.factorial(d[list(d.keys())[0]]) // (2 * math.factorial(d[list(d.keys())[0]] - 2)))
  quit()

l = list(d.values())

res = 1

for i in l:
  res *= (i + 1)

res -= 1

print(res)
