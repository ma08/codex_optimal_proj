

n,m = map(int,input().split())
a = list(map(int,input().split()))

# Median is the middle element of a sorted array
# If array length is even, median is the average of two middle elements

# Find the number of times m appears in the array
# If m appears in the array, then it is also a median
# The number of times m appears in the array is the number of times it appears as a median

m_count = a.count(m)

# Find the number of times m appears as a median
# If m is the median, then the number of elements less than m is equal to the number of elements greater than m
# The number of elements less than m is equal to the number of elements less than or equal to m minus the number of elements equal to m
# The number of elements greater than m is equal to the number of elements greater than or equal to m minus the number of elements equal to m
# The number of elements less than or equal to m is equal to the index of m in the sorted array
# The number of elements greater than or equal to m is equal to the number of elements in the array minus the index of m in the sorted array
# The number of times m appears as a median is equal to the number of elements less than m times the number of elements greater than m

# Sort the array
a.sort()

# Find the number of times m appears as a median
median_count = 0
if m in a:
    median_count = a.index(m)*(n-a.index(m))

print(m_count+median_count)