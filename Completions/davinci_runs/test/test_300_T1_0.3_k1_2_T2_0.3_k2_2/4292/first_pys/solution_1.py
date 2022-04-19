

def main():
    n, k = map(int, input().split())
    prices = sorted(list(map(int, input().split())))
    print(sum(prices[:k]))

if __name__ == '__main__':
    main()