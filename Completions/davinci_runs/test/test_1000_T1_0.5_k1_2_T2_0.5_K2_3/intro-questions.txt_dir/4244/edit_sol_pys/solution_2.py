

def main():
    """
    N = 2
    X = [1,4]
    """
    N = int(input())
    X = [int(x) for x in input().split()]  # list comprehension

    # Xの中央値が最小となるようにする
    X.sort()
    #print(X)
    if N % 2 == 0:
        # 偶数
        median = (X[N//2-1] + X[N//2])/2
    else:
        # 奇数
        median = X[N//2]

    #print(median)
    ans = 0
    for x in X:
        ans += (x-median)**2
    print(ans)

if __name__ == '__main__':
    main()
