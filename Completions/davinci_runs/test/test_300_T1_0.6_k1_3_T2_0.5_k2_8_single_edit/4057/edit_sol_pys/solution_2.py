

n = int(input())
arr = list(map(int, input().split()))

# n = 6
# arr = [1, 2, 4, 3, 3, 2]

def get_min_pockets(n, arr):
  result = 0
  d = {}
  for i in arr:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  for i in d:
    if d[i] % 2 != 0:
      result += 1
  return result

print(get_min_pockets(n, arr))
