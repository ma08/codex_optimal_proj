

# SOLUTION

n = int(input())
a = list(map(int, input().split()))

d = {}

for i in a:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1
l = list(d.values())


if len(d) == 1:
  print(l[0] * (l[0] - 1))
  quit()

res = 1

for i in l:
  res *= (i + 1)

res -= 1

print(res)
