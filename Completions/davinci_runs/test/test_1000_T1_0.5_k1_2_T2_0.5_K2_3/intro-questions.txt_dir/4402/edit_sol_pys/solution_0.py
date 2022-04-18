

a, b = map(int, input().split()) # A: 年齢, B: 料金

if a >= 13: # 13歳以上ならば
    print(b) # 料金をそのまま出力
elif a >= 6: # 6歳以上13歳未満ならば
    print(b // 2) # 料金の半額を出力
else: # それ以外ならば
    print(0) # 料金を0円として出力
