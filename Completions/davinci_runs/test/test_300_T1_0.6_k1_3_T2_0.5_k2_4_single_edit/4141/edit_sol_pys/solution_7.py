

def main():
    num = int(input())  # 入力
    for i in input().split():  # スペース区切りで入力
        if int(i) % 2 == 0 and int(i) % 3 != 0 and int(i) % 5 != 0:  # 条件分岐
            print("DENIED")  # 出力
            exit()  # 終了
    print("APPROVED")  # 出力

if __name__ == '__main__':
    main()
