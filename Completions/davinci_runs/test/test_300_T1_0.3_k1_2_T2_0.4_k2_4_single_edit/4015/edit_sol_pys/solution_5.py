
def main():
    n, m = map(int, input().split())  # n: 初期値, m: 目標値
    if n == m:
        print(0)  # 目標値と初期値が同じ場合は何もしなくても目標値になるため0
        return  # 終了
    if n > m:  # 目標値より初期値が大きい場合は到達不可能
        print(-1)  # 到達不可能なら-1
        return  # 終了
    count = 0
    while n < m:
        if n * 2 <= m:  # 倍にした方が目標値に近い場合は倍にする
            n *= 2  # 倍にする
        elif n * 3 <= m:  # 倍にした方が目標値に遠い場合は3倍にする
            n *= 3  # 3倍にする
        else:
            return  # 終了
        count += 1  # 回数を加算
    print(count)  # 回数を出力

if __name__ == '__main__':
    main()
