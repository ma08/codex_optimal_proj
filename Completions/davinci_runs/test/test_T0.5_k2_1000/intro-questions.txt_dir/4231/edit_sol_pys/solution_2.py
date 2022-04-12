

def calc_remaining_cells(H, W, h, w):  # H: 高さ, W: 幅, h: 高さ, w: 幅
    return (H-h)*(W-w)  # 高さHから高さhを引いたものと、幅Wから幅wを引いたものを掛け合わせる

H, W = map(int, input().split())  # H, Wを取得
h, w = map(int, input().split())  # h, wを取得

print(calc_remaining_cells(H, W, h, w))  # 残りのマス数を出力
