

def calc_remaining_cells(H, W, Hh, Ww):
    return (H-Hh)*(W-Ww)

H, W = map(int, input().split())
Hh, Ww = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
