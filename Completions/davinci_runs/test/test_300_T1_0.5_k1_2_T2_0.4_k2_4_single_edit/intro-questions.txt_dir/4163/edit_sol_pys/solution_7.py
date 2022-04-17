

def main():
    n = int(input())  # 行数
    cnt = 0
    for i in range(n):
        d1, d2 = map(int, input().split())  # 列ごとに数字を取得
        if d1 == d2:
            cnt += 1  # 同じ数字が続いた場合カウントを増やす
        else:
            cnt = 0
        if cnt >= 3:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
