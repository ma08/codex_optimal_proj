
k = int(input())

i = 1
while 2**i < k:
    i += 1

smallest_power = 2**i

if smallest_power == k:
    print(k, 0)
else:
    # Otherwise, we need to break the bar of size smallest_power into two smaller bars
    # We can do this repeatedly until we have a bar of size k.
    num_breaks = 1
    while smallest_power > k:
        smallest_power = smallest_power // 2
        num_breaks += 1
    print(smallest_power, num_breaks)
