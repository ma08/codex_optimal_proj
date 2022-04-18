

# input a
a, b, c, d = map(int, input().split()) # 複数の変数に代入

# output
print(max(0, min(b, d) - max(a, c))) # max: 最大値を返す
                                    # min: 最小値を返す
