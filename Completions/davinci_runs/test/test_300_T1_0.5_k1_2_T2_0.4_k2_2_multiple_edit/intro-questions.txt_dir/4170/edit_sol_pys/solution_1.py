
def main():
    n = int(input()) # 数字を取得してnに代入
    h = list(map(int, input().split())) # 数字を取得してリストに代入
    ans = 0
    while n > 0: # nが0より大きい間
        n -= 1 # nを1減らす
        if n == 0: # nが0なら
            ans += 1
            break
        if h[n] >= h[n-1]: # h[n]がh[n-1]以上なら
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
