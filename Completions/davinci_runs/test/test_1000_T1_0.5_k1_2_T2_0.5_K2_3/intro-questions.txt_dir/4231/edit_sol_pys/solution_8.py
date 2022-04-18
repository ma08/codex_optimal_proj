

def calc_remaining_cells(H, W, h, w): # 関数を定義
    # 残りのセル数を計算
    return (H-h)*(W-w) # return 文を追加

H, W = map(int, input().split()) # 変数を定義
h, w = map(int, input().split()) # 変数を定義

print(calc_remaining_cells(H, W, h, w)) # 関数を呼び出し
