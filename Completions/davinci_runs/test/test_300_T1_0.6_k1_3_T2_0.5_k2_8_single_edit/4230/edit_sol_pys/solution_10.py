

x, n = map(int, input().split())  # 入力を整数に変換
p = set(map(int, input().split()))  # 入力を整数に変換してset型の変数に代入

for i in range(0, 200):  # 0~200までの整数をiに代入
    if x - i not in p:  # x - iがpに含まれていない場合
        print(x - i)
        exit()
    elif x + i not in p:
        print(x + i)
        exit()
