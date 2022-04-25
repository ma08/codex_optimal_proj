
def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:  # 同じ数字が出たらカウントを増やす
            cnt += 1
        else:  # 違う数字が出たらカウントをリセット
            cnt = 0
        if cnt >= 3:  # カウントが3以上になったらYesを出力して終了
            print("Yes")
            break
    else:
        print("No")


if __name__ == '__main__':
    main()
