

def main():
    n = int(input())
    a = list(input().split())
    f = list(map(int, input().split()))
    f = [0] + f  # 0番目の要素を0にする

    for i in range(n):
        a[i] = str(f[int(a[i])])  # 入力された文字列を数値に変換して数値を取得

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
