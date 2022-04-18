

def calc_remaining_cells(h, w, H, W):
    return (H - h) * (W - w)

h, w = map(int, input().split())  # h:高さ, w:幅
H, W = map(int, input().split())  # H:高さ, W:幅

print(calc_remaining_cells(H, W, h, w))
