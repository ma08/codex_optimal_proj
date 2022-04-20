

def main():
    n, k = map(int, input().split())  # 入力を2つ受け取る
    A = list(map(int, input().split()))  # 入力を受け取ってリストにする
    i, j = 0, n-1  # i,jを初期化
    ans = 0  # ansを初期化
    while i <= j:  # iがj以下の間繰り返す
        if A[i] > k and A[j] > k:  # A[i]とA[j]がkより大きい時
            break  # 抜ける
        elif A[i] <= k and A[j] <= k:  # A[i]とA[j]がk以下の時
            ans += 2  # ansに2を足す
            i += 1  # iに1を足す
            j -= 1  # jから1を引く
        elif A[i] <= k:  # A[i]がk以下の時
            ans += 1  # ansに1を足す
            i += 1  # iに1を足す
        else:  # それ以外の時
            ans += 1  # ansに1を足す
            j -= 1  # jから1を引く
    print(ans)  # ansを出力する

if __name__ == '__main__':
    main()
