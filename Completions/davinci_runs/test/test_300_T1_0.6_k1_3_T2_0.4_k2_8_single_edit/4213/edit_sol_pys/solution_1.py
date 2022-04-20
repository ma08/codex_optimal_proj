

def main():
    n = int(input())
    a = list(map(int, input().split()))
    lmin = a[0] # 最小値
    rmax = a[-1] # 最大値
    ans = 0
    for i in range(1, n):
        ans = max(ans, max(a[i] - lmin, rmax - a[i])) # 左側の最小値との差と右側の最大値との差の大きい方をansに入れる
        lmin = min(lmin, a[i]) # 左側の最小値を更新する
        rmax = max(rmax, a[i]) # 右側の最大値を更新する
    print(ans)

if __name__ == '__main__':
    main()
