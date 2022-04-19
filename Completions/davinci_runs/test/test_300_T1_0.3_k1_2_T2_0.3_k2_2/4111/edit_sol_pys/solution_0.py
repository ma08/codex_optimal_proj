

def main():
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0  # 奇数番目の合計
    even = 0  # 偶数番目の合計
    count = 0
    for i in range(n):  # 奇数番目と偶数番目の合計を計算
        if i % 2 == 0:  # 偶数番目
            even += a[i]  # 偶数番目の合計
        else:  # 奇数番目
            odd += a[i]  # 奇数番目の合計
    for i in range(n):
        if i % 2 == 0:  # 偶数番目
            even -= a[i]  # 偶数番目の合計からi番目を引く
        else:  # 奇数番目
            odd -= a[i]  # 奇数番目の合計からi番目を引く
        if even == odd:
            count += 1  # 奇数番目の合計と偶数番目の合計が等しければカウント
        if i % 2 == 0:  # 偶数番目
            even += a[i]  # 偶数番目の合計にi番目を足す
        else:  # 奇数番目
            odd += a[i]  # 奇数番目の合計にi番目を足す
    print(count)

if __name__ == "__main__":
    main()
