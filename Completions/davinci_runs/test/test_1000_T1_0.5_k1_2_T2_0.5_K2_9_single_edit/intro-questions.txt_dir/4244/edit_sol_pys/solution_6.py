
def main():
    N = int(input())
    X = [int(x) for x in input().split()]

    # Xの中央値が最小となる
    X.sort()

    if N % 2 == 0:
        # 偶数
        median = (X[N//2-1] + X[N//2])/2
    else:
        # 奇数
        median = X[N//2]

    ans = 0
    for x in X:
        ans += (x-median)**2
    print(ans)

if __name__ == '__main__':
    main()
