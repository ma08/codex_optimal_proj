

def main():
    n = int(input())
    a = [int(i) for i in input().split()]  # 標準入力
    b = [int(i) for i in input().split()]  # 標準入力

    if a == [0] * n:  # n個の0が入ったリスト
        print(0)
        return
    if b == [0] * n:  # n個の0が入ったリスト
        print(n)
        return

    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        if a[i] * b[n - 1 - i] > 0:
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
