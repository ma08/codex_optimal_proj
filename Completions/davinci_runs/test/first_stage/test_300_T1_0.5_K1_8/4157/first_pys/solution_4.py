

n = int(input())
a = list(map(int, input().split()))

# find the starting number
for i in range(n):
  if a[i] % 3 == 0:
    x = a[i]
    a[i] = -1
    break

# find the other numbers
for i in range(n-1):
  if x % 2 == 0:
    x /= 3
    for j in range(n):
      if a[j] == x:
        a[j] = -1
        break
  else:
    x *= 2
    for j in range(n):
      if a[j] == x:
        a[j] = -1
        break

# print the result
for i in range(n):
  if a[i] != -1:
    print(a[i], end=' ')