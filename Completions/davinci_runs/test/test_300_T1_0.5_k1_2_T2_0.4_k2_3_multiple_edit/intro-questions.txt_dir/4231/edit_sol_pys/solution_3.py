
def calc_remaining_cells(h, w, H, W):
    return (h - H) * (w - W)


H, W = map(int, input().split())  # 入力
h, w = map(int, input().split())  # 入力

print(calc_remaining_cells(h, w, H, W))
