def calc_remaining_cells(H, W, h, w):
    return (H - h) * (W - w)


H, W = map(int, input().split())  # splitしてintに直してリストに格納
h, w = map(int, input().split())  # splitしてintに直してリストに格納

print(calc_remaining_cells(H, W, h, w))
