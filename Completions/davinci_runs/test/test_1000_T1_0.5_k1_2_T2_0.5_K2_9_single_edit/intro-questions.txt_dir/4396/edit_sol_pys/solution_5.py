

def main():
    N = int(input())
    s = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            s += x
        elif u == 'BTC':
            s += x * 380000.0
    print(s)

if __name__ == '__main__':
    main()
