

def main():
    n = int(input())  # 1行目の入力を数値として取得
    a = list(map(int, input().split()))  # 2行目の入力を数値として取得
    odd = 0  # 奇数番目の合計値
    even = 0  # 偶数番目の合計値
    count = 0  # 合計値が等しい場合の数
    for i in range(n):  # 奇数番目と偶数番目の合計値を求める
        if i % 2 == 0:  # 偶数番目の場合
            even += a[i]  # 偶数番目の合計値に加算
        else:  # 奇数番目の場合
            odd += a[i]  # 奇数番目の合計値に加算
    for i in range(n):  # 合計値が等しい場合の数を求める
        if i % 2 == 0:  # 偶数番目の場合
            even -= a[i]  # 偶数番目の合計値から減算
        else:  # 奇数番目の場合
            odd -= a[i]  # 奇数番目の合計値から減算
        if even == odd:  # 偶数番目の合計値と奇数番目の合計値が等しい場合
            count += 1  # 合計値が等しい場合の数を加算
        if i % 2 == 0:  # 偶数番目の場合
            even += a[i]  # 偶数番目の合計値に加算
        else:  # 奇数番目の場合
            odd += a[i]  # 奇数番目の合計値に加算
    print(count)  # 合計値が等しい場合の数を出力

if __name__ == "__main__":
    main()
