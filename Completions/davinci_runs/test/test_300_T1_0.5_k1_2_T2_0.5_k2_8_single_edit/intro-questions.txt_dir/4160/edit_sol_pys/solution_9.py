

def main():
    x = int(input())  # 入力された整数をxに格納
    count = 0
    balance = 100  # 最初の所持金
    while balance < x:  # 入力された整数より所持金が少ない間
        count += 1  # 1円を入れる
        balance += 1  # 所持金を1円増やす
    print(count)  # カウントに入れた回数を出力

if __name__ == '__main__':
    main()
