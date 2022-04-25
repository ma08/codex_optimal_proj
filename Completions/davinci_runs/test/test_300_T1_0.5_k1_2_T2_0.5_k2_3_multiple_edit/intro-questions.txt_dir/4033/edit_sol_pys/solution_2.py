

def main():
    a, b = map(int, input().split())  # a, b はそれぞれ横、縦の長さ

    if a == b:  # 正方形なら、面積は 4 * a
        print(4 * a)
        return

    if a < b:  # 横が縦より短い場合は入れ替える
        a, b = b, a

    # a > b が保証される
    if (a + b) % 3 == 0:  # 縦と横の辺の長さの和が 3 の倍数なら、面積は 2 * (a + b) / 3
        print(2 * (a + b) // 3)
    else:  # そうでないなら、面積は 2 * (a + b) / 3 + 1
        print(2 * (a + b) // 3 + 1)


if __name__ == "__main__":
    main()
