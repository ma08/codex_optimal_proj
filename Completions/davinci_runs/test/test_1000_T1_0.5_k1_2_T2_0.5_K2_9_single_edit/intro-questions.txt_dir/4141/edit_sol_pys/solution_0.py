

n = int(input())  # 数字の数を取得
num = [int(i) for i in input().split()]  # 各数字を取得

for i in num:  # 全ての数字に対して
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:  # 偶数かつ3の倍数でも5の倍数でもない数字が存在する場合
        print("DENIED")
        exit()

print("APPROVED")
