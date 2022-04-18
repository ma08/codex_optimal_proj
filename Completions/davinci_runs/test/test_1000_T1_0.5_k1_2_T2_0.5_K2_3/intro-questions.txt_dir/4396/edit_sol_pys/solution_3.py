
def main():
    N = int(input())
    sums = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            sums += x
        elif u == 'BTC':
            sums += x * 380000.0
    print(sums)

if __name__ == '__main__':
    main()
