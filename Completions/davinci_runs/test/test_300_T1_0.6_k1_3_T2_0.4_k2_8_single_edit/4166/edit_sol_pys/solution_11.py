

def main():
    n, m = map(int, input().split())
    a = [0] * n  # 初期値は0
    for i in range(m):
        s, c = map(int, input().split())
        a[s - 1] = c
    for i in range(n):
        if i == 0 and a[i] == 0:  # 先頭が0の場合はNG
            print(-1)  # NG
            exit()  # 終了
        elif i == 0 and a[i] != 0:  # 先頭が0でない場合
            print(a[i], end="")  # 出力
        else:
            print(a[i], end="")
    print("")

if __name__ == '__main__':
    main()
