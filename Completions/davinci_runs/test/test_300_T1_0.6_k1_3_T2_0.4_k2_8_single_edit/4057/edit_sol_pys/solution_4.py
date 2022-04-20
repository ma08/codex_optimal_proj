

# n = int(input())

# def get_min_pockets(n, arr):
#   d = {}
#   for i in arr:
#     if i in d:
#       d[i] += 1
#     else:
#       d[i] = 1
#   return len(d)

# print(get_min_pockets(n, arr))
# arr = list(map(int, input().split()))

n = 6
arr = [1, 2, 4, 3, 3, 2]

def get_min_pockets(n, arr, d):
  if n == 0:
    return len(d)
  else:
    if arr[n-1] in d:
      d[arr[n-1]] += 1
    else:
      d[arr[n-1]] = 1
    return get_min_pockets(n-1, arr, d)

print(get_min_pockets(n, arr, {}))
