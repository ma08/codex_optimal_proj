a, b, c = map(int, input().split())  # 文字列を数値に変換
if a <= c <= b:  # a <= c <= b が成り立つかどうか
    print('Yes')  # Yesを出力
else:  # a <= c <= b が成り立たない場合
    print('No')  # Noを出力
