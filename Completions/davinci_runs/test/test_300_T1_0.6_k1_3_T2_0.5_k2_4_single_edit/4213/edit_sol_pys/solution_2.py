

def main():
    n = int(input())  # n個の数字を入力
    a = list(map(int, input().split()))  # n個の数字をリストに格納
    lmin = a[0]  # 最初の要素を最小値として代入
    rmax = a[-1]  # 最後の要素を最大値として代入
    ans = 0  # 答えを0で初期化
    for i in range(1, n):  # 1からn-1までのループ
        ans = max(ans, max(a[i] - lmin, rmax - a[i]))  # 一番大きい値をansに代入
        lmin = min(lmin, a[i])  # 最小値を更新
        rmax = max(rmax, a[i])  # 最大値を更新
    print(ans)  # 答えを出力

if __name__ == '__main__':
    main()
