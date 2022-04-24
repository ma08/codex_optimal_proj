


def main():
    a, b, c, d = [int(x) for x in input().split()]  # a,b,c,dを受け取る
    count = 0

    for i in range(a, b + 1):  # aからbまでループ
        if i % c != 0 and i % d != 0:  # cまたはdの倍数でないならカウント
            count += 1

    print(count)  # 答えを出力


if __name__ == '__main__':
    main()
