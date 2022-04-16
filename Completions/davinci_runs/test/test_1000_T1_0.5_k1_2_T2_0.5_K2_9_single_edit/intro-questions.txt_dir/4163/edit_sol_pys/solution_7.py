

def main():
    n = int(input())  # データ数を取得
    cnt = 0  # 同じ数字が続いた数
    for i in range(n):  # データ数分繰り返す
        d1, d2 = map(int, input().split())  # 入力を2つに分ける
        if d1 == d2:  # d1とd2が同じ数字なら
            cnt += 1  # 同じ数字が続いた数を増やす
        else:  # d1とd2が同じ数字じゃないなら
            cnt = 0  # 同じ数字が続いた数を0にする
        if cnt >= 3:  # 同じ数字が続いた数が3以上なら
            print("Yes")  # Yesを出力
            break  # 繰り返しから抜ける
    else:  # 繰り返しが終わったら
        print("No")  # Noを出力

if __name__ == '__main__':
    main()
