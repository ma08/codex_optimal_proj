

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # if a == [0] * n:
    #     print(0)
    #     return
    # if b == [0] * n:
    #     print(n)
    #     return
    
    # a.sort()
    # b.sort()
    # ans = 0
    # for i in range(n):
    #     if a[i] * b[n - 1 - i] > 0:
    #         break
    #     else:
    #         ans += 1
    # print(ans)
    print(a)
    print(b)

if __name__ == '__main__':
    main()
