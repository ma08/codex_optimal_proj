

def main():
    n, r = map(int, input().split())  # n: 部屋の数, r: 半径
    a = list(map(int, input().split()))  # a: 部屋の状態
    ans = 0
    for i in range(n):
        if a[i] == 1:  # 部屋が照らされている場合
            continue
        for j in range(1, r + 1):  # 半径の分だけ照らす
            if i - j < 0 or i + j >= n:  # 半径の分だけ照らすと壁に当たる場合
                break
            if a[i - j] == 1 or a[i + j] == 1:
                a[i] = 1
                ans += 1
                break
            else:
                print(-1)
                return
    print(ans)

main()
