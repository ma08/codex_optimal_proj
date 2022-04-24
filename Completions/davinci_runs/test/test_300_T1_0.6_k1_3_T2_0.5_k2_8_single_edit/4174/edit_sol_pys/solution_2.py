

def main():
    n, x = map(int, input().split())  # 入力
    l = list(map(int, input().split()))  # 入力
    s = 0  # 累積和
    cnt = 0
    for i in range(n):  # 全ての累積和を計算する
        s += l[i]
        if s <= x:  # 累積和がx以下ならカウントする
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
