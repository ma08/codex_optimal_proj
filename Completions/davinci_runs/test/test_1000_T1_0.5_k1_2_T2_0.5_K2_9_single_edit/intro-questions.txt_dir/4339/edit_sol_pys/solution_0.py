

# -----Solution-----

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Sort the a and b lists in ascending order.
a.sort()
b.sort()

# Initialize the count to 0.
count = 0

# Use two pointers to iterate through the sorted lists.
i = 0
j = 0

# Iterate through the two lists
while i < n and j < n:
    # If the sum of the two values is greater than the sum of the two values in the other list,
    # increase the count by the number of remaining values in the other list
    if a[i] + a[j] > b[i] + b[j]:
        count += n - j
        i += 1
    # Otherwise, increase the index of the second list
    else:
        j += 1

print(count)
