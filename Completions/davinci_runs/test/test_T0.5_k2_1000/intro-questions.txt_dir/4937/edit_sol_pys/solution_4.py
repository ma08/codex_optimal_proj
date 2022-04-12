

def main():
    n, a = map(int, input().split())  # n: 個数, a: 容量
    v = list(map(int, input().split()))  # v: 価値のリスト
    w = list(map(int, input().split()))  # w: 重さのリスト
    vw = [(v[i], w[i]) for i in range(n)]  # 価値と重さのタプルのリスト
    vw.sort(key=lambda x: x[0] / x[1], reverse=True)  # 価値密度の昇順にソート
    i = 0
    while a > 0 and i < n:
        if a >= vw[i][1]:  # 入れられるなら入れる
            a -= vw[i][1]
            i += 1
        else:
            break
    print(sum([vw[j][0] for j in range(i)]))

if __name__ == "__main__":
    main()
