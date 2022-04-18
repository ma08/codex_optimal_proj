
def main():
    x = int(input())  # 目標金額
    count = 0  # 手数料を累積する変数
    balance = 100  # 手数料を累積する変数
    while balance < x:  # 現在の手数料が目標金額より小さい間
        count += 1  # 手数料を累積する
        balance += 1  # 手数料を累積する
    print(count)  # 手数料を累積する変数を出力

if __name__ == '__main__':
    main()
