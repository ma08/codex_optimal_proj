

def main():
    x = int(input())
    if x >= 500:
        coins = (x // 500) * 1000 + (x % 500) // 5 * 5
    else:
        coins = x // 5 * 5

    print(coins)

if __name__ == '__main__':
    main()
