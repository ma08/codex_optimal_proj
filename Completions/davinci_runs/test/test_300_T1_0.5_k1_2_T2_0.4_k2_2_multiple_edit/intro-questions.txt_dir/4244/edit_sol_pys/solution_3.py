

def main():
    n = int(input())
    x = [int(x) for x in input().split()]

    # Xの中央値が最小となるようにソート
    x.sort()
    #print(x)
    if n % 2 == 0:
        # 偶数
        median = (x[n//2-1] + x[n//2])/2
    else:
        # 奇数
        median = x[n//2]

    #print(median)
    ans = 0
    for i in x:
        ans += (i-median)**2
    print(ans)

if __name__ == '__main__':
    main()
