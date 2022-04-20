

def main():
    x = int(input())
    coins = (x // 500) * 1000 + (x % 500) // 5 * 5
    print(coins)

if __name__ == '__main__':
    main()
