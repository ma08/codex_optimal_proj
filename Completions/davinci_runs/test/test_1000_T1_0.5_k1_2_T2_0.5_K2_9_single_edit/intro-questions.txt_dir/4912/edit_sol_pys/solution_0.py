

def main():
    h, w, n = map(int, input().split())  # 一行目を取得
    bricks = list(map(int, input().split()))  # 二行目を取得
    i = 0
    for _ in range(h):
        layer = 0  # 層を初期化
        while layer + bricks[i] <= w:
            layer += bricks[i]
            i += 1
            if i == n:
                print("YES")
                return
        if layer == 0:  # この層に積めるブロックがない
            print("NO")
            return
    print("NO")

if __name__ == "__main__":
    main()
