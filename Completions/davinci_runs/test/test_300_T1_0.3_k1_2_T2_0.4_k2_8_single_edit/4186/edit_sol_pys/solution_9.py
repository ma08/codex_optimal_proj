

def main():
    n = int(input())  # 数列の長さ
    a = list(map(int, input().split()))  # 数列
    a.sort()  # 昇順ソート
    ans = 0  # 差分の総和
    while len(a) > 1:  # 数列が1つになるまで
        diff = a[0] - a[-1]  # 差分
        if diff > 0:  # 差分が正
            ans += diff  # 差分を足す
            a[-1] += diff  # 差分を足した値を代入
        else:  # 差分が0
            a.pop()  # 差分が0なので数列から最後の要素を削除
    print(ans)  # 差分の総和を出力

if __name__ == "__main__":
    main()
