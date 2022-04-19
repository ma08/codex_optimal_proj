

def main():
    n = int(input())  # 数列の長さ
    a = list(map(int, input().split()))  # 数列
    odd = 0  # 奇数番目の和
    even = 0  # 偶数番目の和
    count = 0  # 切り替え回数
    for i in range(n):  # 奇数番目の和と偶数番目の和を計算
        if i % 2 == 0:  # 偶数番目
            even += a[i]
        else:  # 奇数番目
            odd += a[i]
    for i in range(n):  # 切り替え回数を計算
        if i % 2 == 0:  # 偶数番目
            even -= a[i]
        else:  # 奇数番目
            odd -= a[i]
        if even == odd:  # 偶数番目の和と奇数番目の和が等しいとき
            count += 1  # 切り替え回数を1増やす
        if i % 2 == 0:  # 偶数番目
            even += a[i]
        else:  # 奇数番目
            odd += a[i]
    print(count)  # 切り替え回数を出力

if __name__ == "__main__":
    main()
