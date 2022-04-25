

def main():
    N = int(input())
    X = [int(x) for x in input().split()]

    # Xの平均値が最小となる
    X.sort()
    #print(X)
    if N % 2 == 0:
        # 偶数
        average = (X[N//2-1] + X[N//2])/2
    else:
        # 奇数
        average = X[N//2]

    #print(average)
    ans = 0
    for x in X:
        ans += (x-average)**2
    print(ans)

if __name__ == '__main__':
    main()
