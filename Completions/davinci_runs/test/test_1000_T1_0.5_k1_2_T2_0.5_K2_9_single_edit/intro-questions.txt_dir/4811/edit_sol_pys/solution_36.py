

k = int(input())

i = 1
while 2**i < k:
    i += 1

smallest_power = 2**i

if smallest_power == k:
    print(k, 0)
else:
    num_breaks = 1
    while smallest_power > k:
        smallest_power = smallest_power // 2
        num_breaks += 1
    print(smallest_power, num_breaks)
