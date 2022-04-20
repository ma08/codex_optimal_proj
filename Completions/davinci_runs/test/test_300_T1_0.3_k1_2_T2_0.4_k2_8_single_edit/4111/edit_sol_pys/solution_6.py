

    # 入力を受け取る
def main():
    n = int(input())
    # 奇数、偶数の合計を初期化
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    # 奇数、偶数の合計を計算
    count = 0
    for i in range(n):
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
        # 奇数、偶数の合計を更新
    for i in range(n):
        if i % 2 == 0:
            even -= a[i]
        else:
        # 奇数、偶数の合計が等しい場合はカウントを増やす
            odd -= a[i]
        if even == odd:
            count += 1
        # 奇数、偶数の合計を更新
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    # 答えを出力
    print(count)

if __name__ == "__main__":
    main()
