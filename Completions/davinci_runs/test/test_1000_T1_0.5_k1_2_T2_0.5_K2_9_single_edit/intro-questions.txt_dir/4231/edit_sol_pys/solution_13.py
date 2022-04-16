

def calc_remaining_cells(H, W, h, w): # 関数の定義
    return (H-h)*(W-w)

H, W = map(int, input().split()) # 入力を2つに分割
h, w = map(int, input().split()) # 入力を2つに分割

print(calc_remaining_cells(H, W, h, w)) # 関数の実行
