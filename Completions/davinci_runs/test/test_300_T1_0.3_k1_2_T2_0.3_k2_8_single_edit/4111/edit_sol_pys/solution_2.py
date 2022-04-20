

def main():
    n = int(input())  # 数列の長さ
    a = list(map(int, input().split()))  # 数列
    odd = 0  # 奇数番目の和
    even = 0  # 偶数番目の和
    count = 0  # 全体で同じ和になる組み合わせの数
    for i in range(n):  # 奇数番目の和と偶数番目の和を求める
        if i % 2 == 0:  # 偶数番目
            even += a[i]  # 偶数番目の和に足す
        else:  # 奇数番目
            odd += a[i]  # 奇数番目の和に足す
    for i in range(n):  # 全体で同じ和になる組み合わせの数を求める
        if i % 2 == 0:  # 偶数番目
            even -= a[i]  # 偶数番目の和から引く
        else:  # 奇数番目
            odd -= a[i]  # 奇数番目の和から引く
        if even == odd:  # 偶数番目の和と奇数番目の和が同じなら
            count += 1  # 全体で同じ和になる組み合わせの数を1増やす
        if i % 2 == 0:  # 偶数番目
            even += a[i]  # 偶数番目の和に足す
        else:  # 奇数番目
            odd += a[i]  # 奇数番目の和に足す
    print(count)  # 全体で同じ和になる組み合わせの数を出力

if __name__ == "__main__":
    main()
