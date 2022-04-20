

def main():
    n = int(input())
    a = list(map(int, input().split()))  # 複数数値入力
    ans = 1
    cur = a[0]
    for i in range(1, n):
        if a[i] <= cur * 2:  # 条件分岐
            ans += 1
        else:
            cur = a[i]
    print(ans)

if __name__ == "__main__":
    main()
