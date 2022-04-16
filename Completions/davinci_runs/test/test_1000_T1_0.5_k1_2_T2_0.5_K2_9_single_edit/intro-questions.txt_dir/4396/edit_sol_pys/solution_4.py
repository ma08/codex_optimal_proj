

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            ans += x
        elif u == 'BTC':
            ans += x * 380000.0
    print(ans)

if __name__ == '__main__':
    main()
