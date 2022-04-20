

def read_ints():
  temp = input().split()
  temp = [int(t) for t in temp]
  return temp

def solve(n, k, a):
  count = 0
  while True:
    min_num = min(a)
    if min_num == 0:
      break
    for i in range(len(a)):
      a[i] = a[i] - min_num
    count += 1
  print(count)

n, k = read_ints()
a = read_ints()
solve(n, k, a)