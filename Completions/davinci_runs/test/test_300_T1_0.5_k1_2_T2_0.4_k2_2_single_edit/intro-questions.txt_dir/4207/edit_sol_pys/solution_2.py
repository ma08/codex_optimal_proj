
def main():
    n = int(input())  # 要素数
    a = [int(i) for i in input().split()]  # 要素
    b = [int(i) for i in input().split()]  # 要素
    
    if a == [0] * n:  # 全ての要素が0の場合
        print(0)
        return
    if b == [0] * n:  # 全ての要素が0の場合
        print(n)
        return
    
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        if a[i] * b[n - 1 - i] > 0:  # 符号が異なるとき
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
