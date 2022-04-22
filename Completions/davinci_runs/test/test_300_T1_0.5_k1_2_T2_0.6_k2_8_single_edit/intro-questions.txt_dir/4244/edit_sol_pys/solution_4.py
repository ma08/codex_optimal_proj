

def median(A):
    """
    Xの中央値が最小となる
    """
    A.sort()
    #print(X)
    if len(A) % 2 == 0:
        # 偶数
        return (A[len(A)//2-1] + A[len(A)//2])/2
    else:
        # 奇数
        return A[len(A)//2]



def main():
    """
    N = 2
    X = [1,4]
    """
    N = int(input())
    X = [int(x) for x in input().split()]

    m = median(X)
    ans = 0
    for x in X:
        ans += (x-m)**2
    print(ans)

if __name__ == '__main__':
    main()
