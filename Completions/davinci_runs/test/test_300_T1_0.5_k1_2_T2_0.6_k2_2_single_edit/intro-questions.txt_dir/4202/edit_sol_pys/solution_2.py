
L, R = map(int, input().split())
if R - L >= 2019:
  print(0)
else:
  a = L % 2019
  b = (R-1) % 2019
  if a < b:
    a, b = b, a
  min_val = 2019
  for i in range(b+1, a+1):
    for j in range(i, a+1):
      min_val = min(min_val, i * j % 2019)
  print(min_val)
