
num = int(input())  # 入力値を変数numに代入
input_list = list(map(int, input().split()))  # 入力値をリストに格納
for i in input_list:  # リストの値を一つずつ取り出し
    if i % 2 == 0:  # 取り出した値が偶数の場合
        if i % 3 != 0 and i % 5 != 0:  # 3でも5でも割り切れない場合
            print("DENIED")  # DENIEDを出力
            exit(0)  # プログラムを終了
print("APPROVED")  # 全ての値が条件を満たした場合はAPPROVEDを出力
