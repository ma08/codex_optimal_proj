

a = int(input())

while (sum([int(x) for x in str(a)])%4 != 0):
  a += 1

print(a)