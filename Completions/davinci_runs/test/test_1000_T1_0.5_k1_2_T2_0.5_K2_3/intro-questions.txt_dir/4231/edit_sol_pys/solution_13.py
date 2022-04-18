

def calc_remaining_cells(H, W, h, w): # 関数を定義
    # 残りのセル数を計算
    return (H - h) * (W - w)

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
