
a, b = map(int, input().split()) # 入力された値をaとbに格納する
consumption = a / 0.08 # 消費量を計算してconsumptionに格納する
if consumption > b / 0.1: # 消費量がb/0.1より大きい場合
    print(int(b / 0.1)) # b/0.1を出力する
elif consumption < a / 0.1: # 消費量がa/0.1より小さい場合
    print(int(a / 0.1)) # a/0.1を出力する
else: # それ以外の場合
    print(int(consumption)) # consumptionを出力する
