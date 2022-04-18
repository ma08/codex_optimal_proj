
# Solution
# get the number of elements

# get the elements and store them in an array
n = int(input())
a = list(map(int, input().split()))

# sort the array
a.sort()

# check if the first and last elements are the same
if a[0] == a[n - 1]:
  print(0)
else:
  # get the difference between the first two elements
  d = a[1] - a[0]
  # iterate through the array, if the difference is not the same between the current element and the previous, return -1
  for i in range(1, n - 1):
    if (a[i + 1] - a[i]) != d:
      print(-1)
      break
  else:
    print(d)
