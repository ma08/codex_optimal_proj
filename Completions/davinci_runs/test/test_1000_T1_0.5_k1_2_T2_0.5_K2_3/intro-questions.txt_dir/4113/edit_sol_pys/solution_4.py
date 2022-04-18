N = int(input())  # 標準入力
for i in range(N // 4 + 1):  # 4の倍数を繰り返す
    for j in range(N // 7 + 1):  # 7の倍数を繰り返す
        if N == i * 4 + j * 7:  # 合計値がNと一致したら
            print("Yes")  # Yesを出力して終了
            exit()  # 終了
print("No")  # 一致しなかったらNoを出力
