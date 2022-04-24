

def main():
    n, k = map(int, input().split())  # n: 席の数 k: 席間隔(k以下の人しか席に着けない)
    A = list(map(int, input().split()))  # A: 参加者の身長
    i, j = 0, n - 1
    ans = 0  # 答え
    while i <= j:  # 席の両端から身長の高い人を探す
        if A[i] > k and A[j] > k:  # 席の両端の人がkを超えていたら終了
            break  # 終了
        elif A[i] <= k and A[j] <= k:  # 両端の人がk以下だったら
            ans += 2  # 席を2つ埋める
            i += 1  # 左端の席を1つ進める
            j -= 1  # 右端の席を1つ戻す
        elif A[i] <= k:  # 左端の人がk以下だったら
            ans += 1  # 席を1つ埋める
            i += 1  # 左端の席を1つ進める
        else:  # 右端の人がk以下だったら
            ans += 1  # 席を1つ埋める
            j -= 1  # 右端の席を1つ戻す
    print(ans)  # 答えを出力


if __name__ == '__main__':
    main()
