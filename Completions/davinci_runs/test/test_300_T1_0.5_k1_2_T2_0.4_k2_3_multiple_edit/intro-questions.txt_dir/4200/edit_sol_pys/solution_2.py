

def main():
    n, m = map(int, input().split()) # n: 人数, m: チーム数
    a = list(map(int, input().split())) # a: 各人の能力値

    if max(a) >= sum(a) / (4 * m): # 能力値の平均値が最大値以上ならば、チームを作れる
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
