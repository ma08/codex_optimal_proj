
#-----Solution-----

n, k = map(int, input().split())
a = list(map(int, input().split()))

# Sort the array in descending order
a.sort(reverse=True)

# Find the maximum number of operations required to make all elements equal
# This is the number of operations required to make the largest element equal to the smallest element
max_ops = a[0] - a[-1]

# Find the minimum number of operations required to make all elements equal
# This is the number of operations required to make the smallest element equal to the largest element divided by 2
min_ops = (a[0] - a[-1]) // 2

# If the minimum number of operations required to make all elements equal is less than the maximum number of operations required to make all elements equal
# Then we can make all elements equal in the minimum number of operations
if min_ops < max_ops:
    print(min_ops)

# If the minimum number of operations required to make all elements equal is greater than or equal to the maximum number of operations required to make all elements equal
# Then we can make all elements equal in the maximum number of operations
else:
    # Find the number of elements that are equal to the largest element
    num_largest = a.count(a[0])

    # If the number of elements that are equal to the largest element is greater than or equal to the number of elements required to be equal
    # Then we can make all elements equal in the maximum number of operations
    if num_largest >= k:
        print(max_ops)

    # If the number of elements that are equal to the largest element is less than the number of elements required to be equal
    # Then we can make all elements equal in the maximum number of operations plus the number of operations required to make the largest element equal to the second largest element
    else:
        print(max_ops + (a[1] - a[0]) // 2)
