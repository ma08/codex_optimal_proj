
def calc_remaining_cells(h, w, H, W):
    return (h - H) * (w - W)

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(h, w, H, W))
