

import math

N = int(input())  # 整数の個数
A = []  # 整数を格納する配列
for i in range(N):  # N回繰り返す
    A.append(int(input()))  # 整数を入力して配列に追加する

for i in A:  # 配列の各要素について
    if i % 2 == 0 and (i % 3 != 0 and i % 5 != 0):  # 偶数かつ3でも5でも割り切れない
        print('DENIED')  # DENIEDを出力して終了
        exit(0)  # プログラムを終了する
print('APPROVED')  # それ以外はAPPROVED
