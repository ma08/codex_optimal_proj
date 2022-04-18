
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # 店にある商品の個数を格納する配列
    offers = []  # 割引券情報を格納する配列
    for i in range(m):
        x, y, c = map(int, input().split())  # 割引券情報を格納
        offers.append([x, y, c])

    # 最初は全ての商品を買う場合の最小金額を求める
    min_cost = sum(a)

    for offer in offers:
        x, y, c = offer
        if a[x-1] + a[y-1] > c:
            min_cost -= a[x-1] + a[y-1]
            min_cost += c

    print(min_cost)


if __name__ == "__main__":
    main()
