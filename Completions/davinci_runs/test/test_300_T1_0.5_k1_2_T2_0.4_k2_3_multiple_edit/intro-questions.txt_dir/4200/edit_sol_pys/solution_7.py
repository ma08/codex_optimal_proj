
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m):  # 自分のスコアが4m人のスコアの平均より大きいか
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
