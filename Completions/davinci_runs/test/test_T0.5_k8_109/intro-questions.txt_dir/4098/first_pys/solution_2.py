

# Solution

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

# sort the array
a.sort()

# get minimum and maximum elements
min_elem = a[0]
max_elem = a[-1]

# check if the minimum and maximum elements are within the threshold
if max_elem - min_elem <= 5:
    print(n)
else:
    # get the middle elements
    mid_elem = a[n//2]
    mid_elem_2 = a[n//2 - 1]
    if mid_elem - min_elem > 5:
        print(n//2)
    else:
        print(n//2 + 1)