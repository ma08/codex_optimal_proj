

def main():
    n = int(input())
    a = list(map(int, input().split()))
    lmin = a[0] # 最小値を先頭の値で初期化
    rmax = a[-1] # 最大値を末尾の値で初期化
    ans = 0
    for i in range(1, n):
        ans = max(ans, max(a[i] - lmin, rmax - a[i])) # ansを更新
        lmin = min(lmin, a[i]) # 最小値を更新
        rmax = max(rmax, a[i]) # 最大値を更新
    print(ans)

if __name__ == '__main__':
    main()
