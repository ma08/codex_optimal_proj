

import math

def main():
    n = int(input())  # 入力
    count = 0  # 変換回数
    while n > 0:  # 入力が0になるまでループ
        if n % 6 == 0:  # 6で割り切れるなら
            n = n // 6  # 6で割る
            count += 1  # 変換回数を1増やす
        elif n % 9 == 0:  # 9で割り切れるなら
            n = n // 9  # 9で割る
            count += 1  # 変換回数を1増やす
        else:  # それ以外なら
            n = n - 1  # 1引く
            count += 1  # 変換回数を1増やす
    print(count)  # 変換回数を出力

if __name__ == '__main__':
    main()  # メイン関数を呼び出す
