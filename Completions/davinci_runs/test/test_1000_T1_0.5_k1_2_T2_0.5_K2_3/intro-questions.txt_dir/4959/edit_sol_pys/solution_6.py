

a = map(int, input().split())  # a = [empty, full, exchange]
soda = 0  # soda
empty = a[0] + a[1]  # empty
while empty >= a[2]:  # loop if empty >= exchange
    empty = empty - a[2] + 1  # empty = empty - exchange + 1
    soda += 1  # soda + 1
print soda  # print soda
