

def main():
    n, c = map(int, input().split())  # 行数、容量
    w = list(map(int, input().split()))  # 各商品の重さ
    fruits = sorted(w)  # 重さの昇順ソート

    i = 0
    total = 0
    while i < n:
        if total + fruits[i] <= c:  # 容量内に収まるなら詰める
            total += fruits[i]
            i += 1
        else:  # 収まらないなら終了
            break

    print(i)

if __name__ == "__main__":
    main()
