

def main():
    n, m = map(int, input().split()) # n人、m問
    a = list(map(int, input().split())) # 各問題の制約

    if max(a) >= sum(a) / (4 * m): # 満点の問題があっても役に立たない場合は"No"
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
