
def main():
    n, m = map(int, input().split())  # 入力
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ans = "Yes"
    for i in range(m):
        if a[i] < sum(a) / (4 * m):
            ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
