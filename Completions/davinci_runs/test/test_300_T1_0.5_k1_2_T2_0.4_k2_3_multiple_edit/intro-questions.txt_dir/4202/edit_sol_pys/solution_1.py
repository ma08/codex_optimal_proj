
L, R = map(int, input().split())

if R - L > 2019:
  print(0)
else:
  min_val = 2019
  for i in range(L, R):
    for j in range(i+1, R+1):
      min_val = min(min_val, (i * j) % 2019)
  print(min_val)
