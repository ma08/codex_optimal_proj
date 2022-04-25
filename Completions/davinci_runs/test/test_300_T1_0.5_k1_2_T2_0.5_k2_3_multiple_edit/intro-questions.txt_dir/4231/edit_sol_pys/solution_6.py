

def calc_remaining_cells(h, w, H, W): # H: 高さ、W: 幅、h: 高さ、w: 幅
    return (H-h)*(W-w) # (H-h) * (W-w)　

h, w = map(int, input().split()) # 高さ、幅
H, W = map(int, input().split()) # H: 高さ、W: 幅

print(calc_remaining_cells(h, w, H, W))
