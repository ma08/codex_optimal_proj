

def main():
    n, k, x = map(int, input().split())  # 入力
    A = list(map(int, input().split()))  # 入力
    if x < k:  # kがxより小さいとき
        print(-1)
        return
    ans = 0  # 初期値
    for i in range(k):  # k回繰り返す
        if i < n:  # iがnより小さいとき
            ans += A[i]  # A[i]を足す
        else:  # それ以外
            ans += x  # xを足す
    print(ans)
    return

if __name__ == '__main__':
    main()
