
# テスト
A, B = map(int, input().split()) # 入力を整数に

if A >= 13: # 13歳以上なら
    print(B) # 割引なし
elif A >= 6: # 6歳以上なら
    print(B // 2) # 半額
else:
    print(0) # それ以外なら０
