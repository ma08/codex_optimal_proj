

def main():
    n, c = map(int, input().split())  # n: 個数 c: キャパ
    w = list(map(int, input().split()))  # w: 重さ
    fruits = sorted(w)  # wをソートしたリスト

    i = 0  # 現在の要素
    total = 0  # 現在の重さ
    while i < n:  # 個数分ループ
        if total + fruits[i] <= c:  # キャパを超えない場合
            total += fruits[i]  # 重さを加える
            i += 1  # 要素をカウント
        else:
            break

    print(i)  # 個数を出力


if __name__ == "__main__":
    main()
