
def calc_remaining_cells(H, W, h, w):  # 引数は全て整数
    return (H-h)*(W-w)  # 小麦の数を返す

H, W = map(int, input().split())
h, w = map(int, input().split())

print(calc_remaining_cells(H, W, h, w))
