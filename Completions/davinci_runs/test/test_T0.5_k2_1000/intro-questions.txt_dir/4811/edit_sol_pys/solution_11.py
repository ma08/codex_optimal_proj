
#!/usr/bin/env python3

def get_bar_size(n):
    return 2 ** (len(bin(n)) - 3)

def get_num_breaks(n):
    bar_size = get_bar_size(n)
    num_breaks = 0
    while bar_size != n:
        bar_size //= 2
        num_breaks += 1
    return num_breaks

n = int(input())
print('{} {}'.format(get_bar_size(n), get_num_breaks(n)))
