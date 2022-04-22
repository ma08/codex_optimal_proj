
# coding: utf-8
n = int(input()) # 入力
if n % 10 in [0, 1, 6, 8]: # 0,1,6,8の場合
    print("pon") # ponを出力
elif n % 10 in [2, 4, 5, 7, 9]: # 2,4,5,7,9の場合
    print("hon") # honを出力
elif n % 10 == 3: # 3の場合
    print("bon") # bonを出力
