

def main():
    n = int(input())  # 手数
    a = int(input())  # 実行時間
    b = int(input())  # 実行時間
    c = int(input())  # 実行時間
    d = int(input())  # 実行時間
    e = int(input())  # 実行時間

    l = [a, b, c, d, e]  # 実行時間リスト
    l.sort()  # 実行時間リストをソート

    if n <= l[0]:  # 実行時間が最小の手数以下なら
        print(1)  # 1回で完了
    else:
        print(2)  # 2回で完了

if __name__ == '__main__':
    main()
