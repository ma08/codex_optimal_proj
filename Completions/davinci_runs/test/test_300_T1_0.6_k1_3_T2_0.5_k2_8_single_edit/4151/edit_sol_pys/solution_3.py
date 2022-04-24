

# SOLUTION 1

n = int(input())
a = list(map(int, input().split()))

d = {}

for i in a:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

if len(d) == 1:
  print(1)
  quit()

l = list(d.values())

res = 1

for i in l:
  res *= (i + 1)

res -= 1

print(res)

# SOLUTION 2

n = int(input())
a = list(map(int, input().split()))

d = {}

for i in a:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

if len(d) == 1:
  print(1)
  quit()

l = list(d.values())

res = 1

for i in l:
  res *= (i + 1)

res -= 1

print(res)
