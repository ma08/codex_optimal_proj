
def main():
    N = int(input())
    s = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            s += x
        elif u == 'BTC':  # 暗号通貨の1BTCは現在価値が380,000円ほど
            s += x * 380000.0
    print(s)


if __name__ == '__main__':
    main()
