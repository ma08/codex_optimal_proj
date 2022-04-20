

def main():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split()))
    f_inv = [0] * 10
    for i in range(1, 10):
        f_inv[f[i - 1]] = i
    a = [f_inv[int(a[i])] for i in range(n)]  # 入力を変換
    a = [str(a[i]) for i in range(n)]  # 文字列に変換
    a = ''.join(a)  # 文字列に変換
    print(a)  # 出力

if __name__ == '__main__':
    main()
