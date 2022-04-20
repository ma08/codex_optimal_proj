

def main():
    n, k = map(int, input().split())  # n: 配列の要素数 k: 判定値
    a = list(map(int, input().split()))  # a: 配列
    i = 0
    j = n - 1
    ans = 0
    while i <= j:
        if a[i] <= k:
            i += 1
            ans += 1
        elif a[j] <= k:
            j -= 1
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
