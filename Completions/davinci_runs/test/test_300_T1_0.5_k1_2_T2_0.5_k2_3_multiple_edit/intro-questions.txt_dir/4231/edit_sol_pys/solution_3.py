

def calc_remaining_cells(H, W, h, w):  # H: 高さ、W: 幅、h: 高さ、w: 幅
    return (H-h)*(W-w)  # (H-h) * (W-w)

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
