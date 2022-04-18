

# k = int(input())
k = 7

# First, find the smallest power of 2 greater than k
# For example, if k = 7, then smallest power of 2 is 8
# If k = 5, then smallest power of 2 is 8
# If k = 9, then smallest power of 2 is 16
i = 1
while 2**i < k:
    i += 1
print(i)

# This is the smallest power of 2 greater than k
print(smallest_power)
smallest_power = 2**i

# If k is a power of 2, then we can just buy a bar of size k
# and not break it at all
if smallest_power == k:
    print(k, 0)
else:
    # Otherwise, we need to break the bar of size smallest_power
    # into two smaller bars
    # We can do this repeatedly until we have a bar of size k
    num_breaks = 1
    while smallest_power > k:
        smallest_power = smallest_power // 2
        num_breaks += 1
    print(smallest_power, num_breaks)
