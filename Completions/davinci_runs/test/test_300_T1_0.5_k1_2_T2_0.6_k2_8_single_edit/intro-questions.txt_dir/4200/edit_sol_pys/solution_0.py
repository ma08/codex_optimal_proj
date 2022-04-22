

def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m): # 各人の買える枚数
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
