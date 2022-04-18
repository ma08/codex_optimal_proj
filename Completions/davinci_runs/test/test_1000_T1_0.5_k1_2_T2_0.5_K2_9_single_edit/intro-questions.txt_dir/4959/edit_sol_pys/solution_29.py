
a = map(int, raw_input().split())
soda = 0
if a[0] >= a[2]:
    empty = a[0] + a[1]
    while empty >= a[2]:
        empty = empty - a[2] + 1
        soda += 1
print soda
