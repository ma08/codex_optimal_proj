
#!/usr/bin/env python3

def get_bar_size(k):
    return 2 ** (len(bin(k)) - 3)

def get_num_breaks(k):
    bar_size = get_bar_size(k)
    num_breaks = 0
    while bar_size != k:
        bar_size //= 2
        num_breaks += 1
    return num_breaks

k = int(input())
print('{} {}'.format(get_bar_size(k), get_num_breaks(k)))
