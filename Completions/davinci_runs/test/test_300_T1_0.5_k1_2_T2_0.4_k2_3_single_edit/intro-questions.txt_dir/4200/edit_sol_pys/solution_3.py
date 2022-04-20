

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m):  # 各数値の合計を4倍した数を割り、その値より大きい数があればYes
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
