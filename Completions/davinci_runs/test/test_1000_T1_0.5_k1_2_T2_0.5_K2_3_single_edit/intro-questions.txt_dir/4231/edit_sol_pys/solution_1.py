

def calc_group(n, groups, uniq_groups, group_size):
    if group_size[n] > 0:
        return group_size[n] - 1

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
