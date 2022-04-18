

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m):
        print("Yes")  # コンテスト開始前にこの問題を解いたので、正解だと思う
    else:
        print("No")


if __name__ == "__main__":
    main()
