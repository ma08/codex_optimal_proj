

n = int(input())  # 入力

if n % 10 in [0, 1, 6, 8]:  # 0, 1, 6, 8 の場合
    print("pon")  # pon を出力
elif n % 10 in [2, 4, 5, 7, 9]:  # 2, 4, 5, 7, 9 の場合
    print("hon")  # hon を出力
elif n % 10 == 3:  # 3 の場合
    print("bon")  # bon を出力
