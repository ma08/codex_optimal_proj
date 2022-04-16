

def calc_remaining_cells(H, W, h, w):  # 引数を定義
    return (H-h)*(W-w)  # 関数を定義

H, W = map(int, input().split())  # 入力を受け取る
h, w = map(int, input().split())  # 入力を受け取る

print(calc_remaining_cells(H, W, h, w))  # 関数を呼び出し
