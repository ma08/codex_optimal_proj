
def main():
    # 入力
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    # 計算
    for i in range(n-1):
        if h[i] >= h[i+1]:
            ans += 1
        else:
            ans += 1
        else:
            break
    # 出力
    print(ans)

if __name__ == '__main__':
    main()
