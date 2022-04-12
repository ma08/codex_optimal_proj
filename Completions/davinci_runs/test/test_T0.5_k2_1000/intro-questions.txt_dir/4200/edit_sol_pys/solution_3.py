
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m):  # 各人の最低点数が4m点以上ならOK
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
