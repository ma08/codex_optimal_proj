
n = int(input())
arr = list(map(int, input().split()))

def get_min_pockets(n, arr):
  d = {}
  for i in arr:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  return len(d)

print(get_min_pockets(n, arr))
