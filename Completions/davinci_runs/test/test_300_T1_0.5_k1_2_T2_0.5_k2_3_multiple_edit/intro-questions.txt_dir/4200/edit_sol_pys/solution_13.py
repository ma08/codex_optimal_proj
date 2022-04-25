

def main():
    N, M = map(int, input().split())  # N: 宝石の数　M: 宝石を取り出す回数
    a = list(map(int, input().split()))  # a: 宝石の個数

    if max(a) >= sum(a) / (4 * M):  # 各宝石を1/4取り出す
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
