
def main():
    n, b, a = map(int, input().split())  # 入力
    s = list(map(int, input().split()))  # 入力
    ans = 0
    while a > 0:
        a -= 1
        ans += 1
    while b > 0:
        b -= 1
        ans += 1
    print(ans)  # 出力


if __name__ == "__main__":
    main()
