

def main():
    n = int(input())  # n 人
    a = sorted(list(map(int, input().split())))  # n 人の点数
    day = 1  # 年数
    while day <= n:  # 年数が n 人より小さい間
        if day > a[day-1]:  # 年数が点数より大きいとき
            break  # 終了
        day += 1  # 年数を増やす
    print(day-1)  # 年数を出力

if __name__ == '__main__':
    main()
