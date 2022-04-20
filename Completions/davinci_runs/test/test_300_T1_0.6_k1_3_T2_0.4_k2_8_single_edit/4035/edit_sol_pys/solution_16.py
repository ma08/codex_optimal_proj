
a, b = map(int, input().split())

consumption = a / 0.08  # 消費電力
if consumption > b / 0.1:  # 消費電力が設定値を超える場合
    print(int(b / 0.1))  # 設定値で計算
elif consumption < a / 0.1:  # 消費電力が設定値を下回る場合
    print(int(a / 0.1))  # 設定値で計算
else:
    print(int(consumption))  # 消費電力で計算
