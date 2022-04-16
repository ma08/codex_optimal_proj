

def main():
    N = int(input())
    _sum = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            _sum += x
        elif u == 'BTC':
            _sum += x * 380000.0
    print(_sum)

if __name__ == '__main__':
    main()
